FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONBUFFERED 1

WORKDIR /django-app

COPY . /django-app/

RUN pip install -U pip
RUN pip install -r requirements.txt

