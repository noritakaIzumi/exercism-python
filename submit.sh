#!/usr/bin/env bash

DIR=$(dirname $(which $0))
NAME=$(echo ${1} | cut -d'/' -f1)

find ${DIR}/${NAME} | grep -E '\.py$' | grep -vE '_test\.py$' | xargs exercism submit
