Movie Similarity
================
**Author:** David Pinto</br>
2020-10-21

> This project implements a recommender system for similar movies based on content and collaborative filtering embedding features.

[![Website ml-eng-proj](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://davpinto.github.io/ml-eng-proj/)

## Documentation

- **Project Proposal** (PDF): [Proposal](https://github.com/davpinto/ml-eng-project/blob/master/proposal/proposal.pdf).
- **Project Report** (PDF): [Report](https://github.com/davpinto/ml-eng-project/blob/master/docs/report.pdf).
- **Project Report** (HTML): [Website](http://davpinto.github.io/ml-eng-proj/).

## Setup

Create a `conda` environment and install all required packages listed in the `env_requirements.txt` file.

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

### Required Pakages

- `numpy` and `pandas` for data cleaning, manipulation and transformation.
- `scipy` for sparse matrices and correlation measures.
- `unidecode` and `nltk` for text manipulation.
- `scikit-learn` for data normalization and text vectorization.
- `vaex` for manipulation of large DataFrames.
- `matplotlib` and `plotnine` for data visualization.
- `lightfm` for collaborative filtering with matrix factorization.
- `faiss` for fast Approximate Nearest Neighbors algorithms.

## Dataset

Take a look at the `data/raw` folder to get instructions on how to download the dataset.

## Notebooks

The project is organized on Jupyter notebooks. Each notebook is self-contained and well documented:

- [1. Data Preparation](https://nbviewer.jupyter.org/github/davpinto/ml-eng-project/blob/master/01-data-preparation.ipynb).
- [2. Exploratory Analysis](https://nbviewer.jupyter.org/github/davpinto/ml-eng-project/blob/master/02-exploratory-analysis.ipynb).
- [3. User Based Similarity](https://nbviewer.jupyter.org/github/davpinto/ml-eng-project/blob/master/03-user-based-similarity.ipynb).
- [4. Content Based Embedding](https://nbviewer.jupyter.org/github/davpinto/ml-eng-project/blob/master/04-content-based-embedding.ipynb).
- [5. Collaborative Fltering Embedding](https://nbviewer.jupyter.org/github/davpinto/ml-eng-project/blob/master/05-collaborative-filtering-embedding.ipynb).
- [6. Similarity Match with ANN](https://nbviewer.jupyter.org/github/davpinto/ml-eng-project/blob/master/06-similarity-match-with-ann.ipynb).
- [7. Performance Evaluation](https://nbviewer.jupyter.org/github/davpinto/ml-eng-project/blob/master/07-performance-evaluation.ipynb).
- [8. Hybrid Approach](https://nbviewer.jupyter.org/github/davpinto/ml-eng-project/blob/master/08-hybrid-approach.ipynb).

## Embedding Visualization

You can play with the movie embedding features using the Embedding Projector [here](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/davpinto/ml-eng-project/master/projector/embedding_projector_config.json). It can take a few seconds to start. But it will be worth it!

Take a look at the `projector` folder to see some results.

## Deploy Web Application

The project provides a [Streamlit](https://www.streamlit.io/) application to play with the movie recommender.

To run it locally:

```bash
make docker-build
make docker-run
```

Congratulations! You have it running on `127.0.0.1:8501`:

------
![](img/application.png)
------

Choose an recommendation algorithm and a movie title to get recommendations of similar movies. I hope you enjoy it!
