# PYTHON
FROM python:3.6.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache \
    build-base \
    gcc \
    libc-dev \
    libffi-dev \
    linux-headers \
    postgresql-dev && \
    mkdir -p /app/src

COPY ./requirements.txt /requirements.txt
COPY ./wait_for_script /bin/wait_for_script

RUN pip install --upgrade pip -r /requirements.txt && \
    chmod 777 -R /bin/wait_for_script

WORKDIR /app/src
