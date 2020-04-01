#!/bin/bash
#
# start_api

# Stop on errors
set -e
set -x

export FLASK_DEBUG=True
export FLASK_APP=backend.py
flask run --host 0.0.0.0 --port 8000