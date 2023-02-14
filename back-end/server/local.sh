#!/bin/bash

# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=endpoints flask run --host=34.228.139.140 --port=8080
