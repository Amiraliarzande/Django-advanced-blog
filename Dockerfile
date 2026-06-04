FROM  docker.abrha.net/python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -i https://mirror.abrha.net/repository/pypi/simple -r requirements.txt


COPY ./core /app


