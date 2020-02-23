FROM python:3.7.6-slim-stretch

WORKDIR /tests

COPY . .

RUN pip install pipenv

RUN pipenv install --dev

RUN useradd user
USER user
