FROM python:3.9-buster



RUN apt-get update
RUN apt-get install build-essential

WORKDIR /lab5
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "jupyter-lab", "--allow-root", "--ip", "0.0.0.0", "--no-browser", "--port", "8888" ]
