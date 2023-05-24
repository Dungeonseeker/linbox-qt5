#!/bin/sh

if [ -d "./venv" ]; then
  echo .
else
  python3 -m venv ./venv
  ./venv/bin/pip install -r requirements.txt
fi
. ./venv/bin/activate

python3 linbox.py
