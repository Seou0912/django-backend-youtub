#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py migrate

# uWSGI: Nginx로 부터 데이터를 받아오면 Django 와 소통을 하는 역할
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi

