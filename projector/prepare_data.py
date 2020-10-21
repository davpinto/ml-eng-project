import pandas as pd
import numpy as np

# Import movie indexes
movie_index = pd.read_pickle('../output/embedding_index.pkl')
    
# Import embedding matrices
with open('../output/embedding_matrix.npy', 'rb') as f:
   content_matrix = np.load(f)
   cb_matrix = np.load(f)
   hybrid_matrix = np.load(f)
   
# Save data
pd.DataFrame(hybrid_matrix).to_csv('embedding_vectors.tsv', sep='\t', header=False, index=False, float_format='%.5f')
movie_index.to_csv('embedding_meta.tsv', sep='\t', header=True, index=False)
