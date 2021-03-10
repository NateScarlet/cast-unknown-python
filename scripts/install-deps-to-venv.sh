#!/bin/bash

set -ex
. ./scripts/activate-venv.sh
python -m pip install -U pip
python -m pip install -r dev-requirements.txt
if [ "${GITHUB_ACTIONS}" == true ]; then 
    python -m pip install tox-gh-actions;
fi
