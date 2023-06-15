FROM python:3.8.14-slim-bullseye

WORKDIR /opt/src

COPY Session2/requirements.txt .

RUN pip install -r requirements.txt /
    && rm -rf /root/.cache/pip

COPY Session2/ .

ENTRYPOINT["/Session2/entrypoint.sh"]

#docker image prune
