#!/bin/bash

CONDA_ENV_NAME="ds-env"
eval "$(conda shell.bash hook)"
conda activate $CONDA_ENV_NAME

pytest test.py