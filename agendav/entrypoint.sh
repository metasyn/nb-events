#!/bin/bash
set -e
nginx
php-fpm7.2
while true; do sleep 1000000; done
