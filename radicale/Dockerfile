FROM python:latest

ENV DIR=/opt/radicale
ENV CONFIG=radicale.conf
ENV RADICALE_CONFIG=$ENV/$CONFIG
WORKDIR $DIR

COPY requirements.txt .
COPY $CONFIG $RADICALE_CONFIG
RUN pip install -r requirements.txt

ENTRYPOINT exec radicale
