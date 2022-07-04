#!/usr/bin/env bash

PYTHON_VERSION="3.9.13"

# Install Python
pyenv install ${PYTHON_VERSION}
pyenv global ${PYTHON_VERSION}
pyenv versions

# Upgrade pip self
pip install --upgrade pip

# Install pip packages
pip install -r requirements.txt
