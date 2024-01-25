FROM python:3.9-buster

RUN apt-get update
RUN apt-get install build-essential
RUN pip install jupyterlab
RUN pip install sklearn matplotlib numpy pandas xgboost nltk sentence_transformers xarray

WORKDIR /lab4

ENTRYPOINT [ "jupyter-lab", "--allow-root", "--ip", "0.0.0.0", "--no-browser", "--port", "8888" ]
