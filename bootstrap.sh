#!/bin/bash
export FLASK_APP=./backend/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0 -p 5001