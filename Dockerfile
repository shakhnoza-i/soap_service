FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  && apt-get upgrade

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /core
WORKDIR /core
COPY ./core /core

RUN addgroup --system soap_user \
    && adduser --system --ingroup soap_user soap_user
RUN chown -R soap_user:soap_user $HOME
RUN chown -R 777 $HOME
USER soap_user