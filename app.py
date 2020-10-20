import streamlit as st
import pandas as pd
import numpy as np
import faiss

'''
Similar Movies Recommender
==========================

Search for a title and get recommendations for similar movies.

------

## Recommendations
'''

def load_data():
    # Import movie indexes
    movie_index = pd.read_pickle('output/embedding_index.pkl')
    
    # Import embedding matrices
    with open('output/embedding_matrix.npy', 'rb') as f:
        content_matrix = np.load(f)
        cb_matrix = np.load(f)
        hybrid_matrix = np.load(f)
    
    # Import ANN indexes
    content_ann = faiss.read_index("output/content_ann.bin")
    cb_ann = faiss.read_index("output/cb_ann.bin")
    hybrid_ann = faiss.read_index("output/hybrid_ann.bin")
    
    data = dict(
        movie_index=movie_index, 
        embedding_matrix=(content_matrix, cb_matrix, hybrid_matrix), 
        ann_index=(content_ann, cb_ann, hybrid_ann)
    )
    
    return data

# Dataset
data = load_data()
movie_index = data['movie_index']

# Movie list
movie_ids = movie_index.index.to_list()
movie_names = movie_index['title'].values
movies = dict(zip(movie_ids, movie_names))

# Parameters
algs = {'Content Based': 0, 'Collaborative Filtering': 1, 'Hybrid': 2}
RECSYS = st.sidebar.radio('Recommender:', list(algs.keys()), key='recommender')
st.sidebar.markdown('------')
K = st.sidebar.slider('Num.Recommendations:', min_value=5, max_value=30, value=10, step=5, key='num_neighbors')
st.sidebar.markdown('------')
MOVIE_ID = st.sidebar.selectbox('Movie:', movie_ids, format_func=lambda x: movies[x], key='selected_movie')

# Selected options
row = movie_index.loc[MOVIE_ID].row
embedding_matrix = data['embedding_matrix'][algs[RECSYS]]
ann_index = data['ann_index'][algs[RECSYS]]

# Recommendations
dist, idx = ann_index.search(embedding_matrix[[row], :], K+1)
neighbors = movie_index.iloc[idx.flatten()].copy()
neighbors['similarity'] = dist.flatten()
st.table(neighbors[['title','similarity']].reset_index(drop=True).drop(0))
