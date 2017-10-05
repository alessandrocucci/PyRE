FROM python:2.7-alpine

MAINTAINER Mikeleg (mgsoluzioni@gmail.com)
COPY ./app /app
COPY ./config-sample.py ./config.py
COPY ./requirements.txt ./
COPY ./run.py ./

WORKDIR ./

RUN apk add --virtual build-dependence \
    && pip install --upgrade pip \
    && pip install gunicorn \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/cache/apk/* \
    && apk del build-dependence

EXPOSE 8080

ENTRYPOINT ["gunicorn","-b","0.0.0.0:8080","app:app"]
