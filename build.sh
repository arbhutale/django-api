#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
python3.9 manage.py collectstatic

python manage.py migrate
