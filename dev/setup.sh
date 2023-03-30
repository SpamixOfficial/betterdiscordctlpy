#!/usr/bin/env sh

python3 -m pip install -r dev/requirements-dev.txt || echo "Could not install the Python requirements. Check your Python & pip installation and be sure that you are in the repository root." && exit 1
pre-commit install