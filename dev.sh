#!/bin/bash
export FLASK_APP=app
source "$(pipenv --venv)/bin/activate"
flask run -h 0.0.0.0 -p 5001