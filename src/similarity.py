import numpy as np
import pandas as pd
import faiss

def create_search_index(embedding):
   x = embedding.to_numpy(copy=False).astype('float32').copy(order='C')
   index = faiss.IndexFlatIP(x.shape[1])
   index.add(x)
   
   return index


def find_top_similar(ids, index, k, embedding, metadata):
   x = embedding.loc[metadata['id'].isin(ids)].to_numpy().astype('float32').copy(order='C')
   y_sim, y_idx = index.search(x, k+1)
   
   y_sim = np.delete(y_sim, 0, axis=1) 
   y_idx = np.delete(y_idx, 0, axis=1)
   
   similars = metadata.loc[y_idx.flatten(), ['id']]
   similars.rename(columns={'id':'id_right'}, inplace=True)
   similars['similarity'] = y_sim.flatten()
   similars['id_left'] = np.repeat(ids, k)
   similars.sort_values(['id_left','similarity'], ascending=[True,False], inplace=True)
   
   return similars


def compute_cosine_similarity(left_id, right_ids, embedding, metadata):
    x = embedding.loc[metadata['id'].isin(left_id)].to_numpy()
    y = embedding.loc[metadata['id'].isin(right_ids)].to_numpy()
    
    cos = np.dot(x, y.T).flatten()
    
    similars = pd.DataFrame({'id_right':right_ids})
    similars['similarity'] = cos
    similars['id_left'] = np.repeat(left_id, len(cos))
    similars.sort_values('similarity', ascending=False, inplace=True)
    
    return similars
