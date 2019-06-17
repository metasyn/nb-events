# FROM janlo/agendav
FROM ubuntu:bionic

EXPOSE 80

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q && \
    apt-get install -y  -q \
    git \
    curl \
    nginx \
    vim \
    php \
    nodejs \
    php-pgsql \
    php-curl \
    php-fpm

 RUN mkdir -p /var/www && cd /var/www && \
    git clone https://github.com/agendav/agendav && cd agendav && \
    npm install && \
    npm run build

#    curl -L -o agendav.tar.gz https://github.com/agendav/agendav/releases/download/2.2.0/agendav-2.2.0.tar.gz && \
#    tar -xzvf agendav.tar.gz && mv agendav-2.2.0 agendav

COPY settings.php /var/www/agendav/web/config
COPY PostgreSqlSchemaManager.php /var/www/agendav/web/vendor/doctrine/dbal/lib/Doctrine/DBAL/Schema/PostgreSqlSchemaManager.php

RUN chmod -R 750 /var/www/agendav/web/var/ && \
    mkdir -p /var/run/php
    # echo "date.timezone=America/Los_Angeles" > /etc/config/php7.2/php.ini

COPY nginx.default /etc/nginx/sites-available/default
COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]