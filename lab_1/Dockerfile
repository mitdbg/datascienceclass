FROM ubuntu:latest

ADD . /lab0
WORKDIR /lab0

RUN apt update
RUN apt install -y python3 python3-pip vim sqlite3
RUN pip3 install -r requirements.txt

CMD ["/bin/bash"]
