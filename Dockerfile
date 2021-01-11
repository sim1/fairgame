# syntax = docker/dockerfile:1.0-experimental
FROM python:3.8-alpine
WORKDIR /app
COPY Pipfile /app

RUN apk add --virtual=.run-deps chromium chromium-chromedriver openssl zlib libjpeg && \
    apk add --virtual=.build-deps build-base musl-dev libffi-dev gcc jpeg-dev zlib-dev openssl-dbg openssl-dev && \
    pip3 install pipenv && \
    pipenv lock --requirements > requirements.txt && \
    pip install -r requirements.txt

ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
COPY . /app
CMD ["python3", "app.py", "amazon", "--headless"]
