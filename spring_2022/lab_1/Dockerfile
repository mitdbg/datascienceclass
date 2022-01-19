FROM ubuntu:latest

ADD . /lab1
WORKDIR /lab1

RUN apt update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt install -y python3 python3-pip vim sqlite3 pkg-config libcairo2-dev libgirepository1.0-dev
RUN pip3 install -r requirements.txt

CMD ["/bin/bash"]
