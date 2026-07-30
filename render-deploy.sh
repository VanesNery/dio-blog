#!/usr/bin/env bash
set -e

poetry run flask --app src.app db upgrade
poetry run gunicorn src.wsgi:app