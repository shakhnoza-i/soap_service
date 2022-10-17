FROM python:3.8-slim-buster

# ensures that the python output is sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output of your application (e.g. django logs)
# in real time. Equivalent to python -u: https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED 1 

# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
# Prevents Python from writing .pyc files to disk
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

# chown all the files to the soap_user     
RUN chown -R soap_user:soap_user $HOME
RUN chown -R 777 $HOME
# Switch to a non-root user
USER soap_user