#!/usr/bin/env bash
# start.sh
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn kites_api.wsgi:application --bind 0.0.0.0:8000 --workers 3
