#!/usr/bin/env bash
# start.sh
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn -n kites_api kites_api.wsgi:application --user www-data --bind 0.0.0.0:8000 --workers 3 --access-logfile - --error-logfile - --log-level info
