FROM python:3.6-slim
MAINTAINER tom@supermaloney.com
COPY . /calculator
WORKDIR /calculator
RUN pytest -v --junitxml=reports/result.xml
CMD tail -f /dev/null
