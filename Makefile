run-jupyter:
	jupyter notebook --no-browser --port=8899
run-app:
	streamlit run app.py
docker-build:
	sudo docker build -t movie-similarity .
docker-run:
	sudo docker run --name movie-similarity -d -p 0.0.0.0:8501:8501 movie-similarity:latest
docker-stop:
	sudo docker stop movie-similarity &&\
	sudo docker rm movie-similarity
