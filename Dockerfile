##
## Python Dockerfile
##
## Pull base image.
FROM python:2-alpine
MAINTAINER Brian Buxton "brbuxton@cisco.com"

RUN pip install --no-cache-dir setuptools wheel

ADD . /app
WORKDIR /app
RUN pip install --requirement /app/requirements.txt
