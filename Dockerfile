FROM python:3.9-slim
MAINTAINER tom@supermaloney.com
ENV POETRY_VERSION=1.1.11

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    build-essential \
    curl

RUN pip install "poetry==$POETRY_VERSION"

COPY . /calculator
WORKDIR /calculator

RUN poetry config virtualenvs.create false && \
  poetry install --no-dev --no-interaction --no-ansi

RUN pytest -v --junitxml=reports/result.xml

CMD tail -f /dev/null
