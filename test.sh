#!/bin/bash

./main.py && git diff --quiet README.md || ( echo "Please run ./main.py and commit changes" && exit 1 )
