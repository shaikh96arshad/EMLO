FROM python:3.9-slim

WORKDIR /opt/src

COPY requirements.txt requirements.tx

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT["python","main.py"]