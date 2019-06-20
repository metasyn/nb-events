FROM python:latest

ENV RADICALE_DIR=/opt/radicale

WORKDIR $RADICALE_DIR

RUN apt-get update -q && apt-get install -y cron vim 
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy meetup-scaper script
COPY meetup_scraper.py .

# Copy cron job settings
COPY meetup-scraper-cron /etc/cron.d/meetup-scraper-cron
RUN chmod 0644 /etc/cron.d/meetup-scraper-cron \
    && crontab /etc/cron.d/meetup-scraper-cron \
    && touch /var/log/cron.log

COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]
