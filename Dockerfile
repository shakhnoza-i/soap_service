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

WORKDIR /usr/src/backend/core

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN addgroup --system soap_user \
    && adduser --system --ingroup soap_user soap_user

COPY ./core /usr/src/backend/core

# Switch to a non-root user
USER soap_user
EXPOSE 8000