# image de base
FROM python:3.8-alpine

# configuration du répertoire de travail
WORKDIR /usr/src/app

# variables d'environnements
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# mise en place de l'environnement virtuel
COPY ./requirements.txt /usr/src/app
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

# installation des dépendances
RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

# copie du projet
COPY . /usr/src/app

# copie des fichiers static du projet
RUN python3 manage.py collectstatic --noinput --clear

# port
EXPOSE 8080

# lancement du projet
CMD python manage.py runserver 0.0.0.0:8080
