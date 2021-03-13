# syntax = docker/dockerfile:1.0-experimental
FROM python:3.8-alpine
WORKDIR /app
COPY Pipfile /app

RUN apk add --virtual=.run-deps chromium chromium-chromedriver openssl zlib libjpeg libxslt libxml2 && \
    apk add --virtual=.build-deps \
    build-base musl-dev libffi-dev gcc jpeg-dev zlib-dev openssl-dbg openssl-dev libxml2-dev libxslt-dev && \
    pip3 install pipenv && \
    pipenv lock --requirements > requirements.txt && \
    pip install -r requirements.txt

ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver \
    CREDENTIAL_FILE=/config/credentials \
    AUTOBUY_CONFIG_PATH=/config/config

COPY . /app
CMD ["python3", "app.py", "amazon", "--headless"]
