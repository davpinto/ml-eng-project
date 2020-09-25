Movie Similarity
================
**Author:** David Pinto</br>
2020-09-23

> This project implements a recommender system for similar movies based on content and collaborative filtering embedding features.

## Setup

Create a `conda` environment:

```
# Create environment
conda create -n movie-similarity -y python=3.7

# Activate environment
conda activate movie-similarity

# Append conda-forge to the list of channels
conda config --append channels conda-forge

# Install dependencies
conda install -y --file requirements.txt

# Add environment to Jupyter
python -m ipykernel install --user --name=movie-similarity
```

## Dataset