# image de base
FROM python:3.8-alpine

# configuration du repertoire de travail
WORKDIR /usr/src/app

# variables d'environnements
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SENTRY_DSN $SENTRY_DSN
ENV HEROKU_APP_NAME $HEROKU_APP_NAME
ENV PORT 8080

# mise en place de l'environnement virtuel
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"


# installation des dépendances
RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps && \
  python3 manage.py collectstatic --noinput --clear


# copie du projet
COPY . /usr/src/app

# lancement du projet
CMD python manage.py runserver 0.0.0.0:$PORT
