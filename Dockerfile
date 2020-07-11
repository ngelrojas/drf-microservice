FROM python:3.8-alpine
MAINTAINER Angel Rojas

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /api
WORKDIR /api
COPY ./api /api

RUN adduser -D user
USER user
