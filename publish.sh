#!/bin/bash

source env/bin/activate
rm -rf build/
rm -rf dist/
python3 setup.py sdist bdist_wheel
twine upload dist/*