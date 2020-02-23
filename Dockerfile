FROM python:3.7.6-slim-stretch

WORKDIR /tests

COPY . .

RUN pip install pytest

ENTRYPOINT ["pytest", "-vv"]