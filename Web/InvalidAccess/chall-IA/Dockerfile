FROM php:7.2-apache
RUN groupadd -g 666 nobodi
RUN useradd -r -u 666 -g nobodi -m nobodi
USER nobodi
RUN mkdir /tmp/whitebox/
COPY ./app/index.php /var/www/index.php
COPY ./app/flag.php /var/www/flag.php
WORKDIR /var/www
CMD php -S 0.0.0.0:4001
