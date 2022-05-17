#!/bin/sh

find requirements/ -name '*.txt' -type f -delete
pip-compile -v -o requirements/requirements.txt requirements/requirements.in