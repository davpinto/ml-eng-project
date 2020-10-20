FROM python:3.7-slim

LABEL maintainer="davpinto"

# Set working dir on container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy data
COPY output/embedding_index.pkl output/embedding_index.pkl
COPY output/embedding_matrix.npy output/embedding_matrix.npy
COPY output/*_ann.bin output/
COPY app.py .

# Export port
EXPOSE 8501

# Start app
CMD ["streamlit", "run", "app.py"]
