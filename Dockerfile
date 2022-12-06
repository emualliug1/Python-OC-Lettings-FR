# image de base
FROM python:3.8-alpine

# configuration du repertoire de travail
WORKDIR /usr/src/app

# variables d'environements
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SENTRY_DSN $SENTRY_DSN
ENV HEROKU_APP_NAME $HEROKU_APP_NAME

# copy project
COPY . .

# installations des dependances
RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps


# port
EXPOSE 8080


CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
