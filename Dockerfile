FROM python:3.7.2-alpine3.8

COPY main.py changelog-parser
COPY requirements.txt requirements.txt

RUN apk add --no-cache curl \
    && pip install -r requirements.txt \
    && chmod +x changelog-parser

CMD sh

