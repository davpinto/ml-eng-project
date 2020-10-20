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
conda install -y --file env_requirements.txt

# Add environment to Jupyter
python -m ipykernel install --user --name=movie-similarity
```

## Dataset

## Embedding Visualization

## Deploy Web Application

## TODO

- Notebooks:

01-data-preparation
02-exploratory-analysis
03-user-similarity
04-content-based-embedding
05-collaborative-filtering-embedding
06-similarity-match-with-ann
07-performance-evaluation
08-hybrid-approach

- Deploy best embeddings on the Embedding Projector

- Streamlit app with Dockerfile for deployment

- Documentation using Rmarkdown to be used as Github Page
