#!/usr/bin/env bash

DIR=$(dirname $(which $0))

NAME=$(echo ${1} | cut -d'/' -f1)

echo ${NAME}
find ${DIR}/${NAME} | grep -E '[^(_test)]\.py$' | xargs echo exercism submit
