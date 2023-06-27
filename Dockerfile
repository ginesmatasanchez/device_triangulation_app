# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY manage.py /usr/src/app/manage.py


RUN pip install --upgrade pip
ARG requirements_file
COPY $requirements_file /device_triangulation_app/requirements.txt

RUN pip freeze > requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /device_triangulation_app


