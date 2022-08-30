FROM python:3.10.4-bullseye
WORKDIR /opt/app/kites_api
COPY . .
RUN apt-get update \
  && apt-get install -y build-essential git libgdal-dev python3-dev libssl-dev\
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/requirements.txt
RUN chown -R www-data:www-data /opt/app
USER www-data
EXPOSE 8000