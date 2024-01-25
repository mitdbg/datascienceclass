FROM python:3.9-buster

RUN apt-get update
RUN apt-get install build-essential
RUN pip install jupyterlab
RUN pip install sklearn matplotlib numpy pandas xgboost

WORKDIR /lab3

ENTRYPOINT [ "jupyter-lab", "--allow-root", "--ip", "0.0.0.0", "--no-browser", "--port", "8888" ]
