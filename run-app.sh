#!/bin/bash

cd project
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

uvicorn main:app --reload --host 0.0.0.0
