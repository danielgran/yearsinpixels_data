#!/bin/zsh
# This file must get called out of the project root.

python3 -m pip install --upgrade pip

mkdir build
pip wheel --wheel-dir ./build .
rm -rf ./src/yearsinpixels_data.egg-info