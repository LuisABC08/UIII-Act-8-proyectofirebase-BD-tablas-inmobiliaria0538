#!/bin/sh
source .venv/bin/activate
cd backend_inmobiliaria38
python manage.py runserver $PORT
