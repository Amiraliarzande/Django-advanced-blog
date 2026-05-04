FROM docker.arvancloud.ir/python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -i https://mirror-pypi.runflare.com/ Django==4.2
RUN pip install -i https://mirror-pypi.runflare.com/ python-decouple
RUN pip install -i https://mirror-pypi.runflare.com/ pillow
RUN pip install -i https://mirror-pypi.runflare.com/ djangorestframework
RUN pip install -i https://mirror-pypi.runflare.com/ markdown
RUN pip install -i https://mirror-pypi.runflare.com/ django-filter
RUN pip install -i https://mirror-pypi.runflare.com/ coreapi
RUN pip install -i https://mirror-pypi.runflare.com/ drf-yasg[validation]
RUN pip install -i https://mirror-pypi.runflare.com/ django-mail-templated
RUN pip install -i https://mirror-pypi.runflare.com/ celery
RUN pip install -i https://mirror-pypi.runflare.com/ redis
RUN pip install -i https://mirror-pypi.runflare.com/ djangorestframework-simplejwt
RUN pip install -i https://mirror-pypi.runflare.com/ django_celery_beat
RUN pip install -i https://mirror-pypi.runflare.com/ django_redis
RUN pip install -i https://mirror-pypi.runflare.com/ gunicorn


COPY ./core /app


