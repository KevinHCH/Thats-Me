#!/bin/bash

# This script allow us to auto-refresh the server(Just for dev mode)
export FLASK_APP=__init__.py
export FLASK_ENV=development
port=$(cat $(pwd)/../.env | grep PORT | head -1 | cut -d '=' -f 2)
flask run --port ${port}