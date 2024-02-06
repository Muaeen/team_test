#!/bin/bash

pip install -r requirements.txt

cd src

uvicorn main:app --host 0.0.0.0 --port 7070 --reload