#!/bin/bash

rm -rf dist
pip install virtualenv
virtualenv -p $(which python3) .build_env
source .build_env/bin/activate
pip install pex wheel
mkdir -p build
pip wheel -w build .
mkdir -p dist
pex -f build -r requirements.txt intra_cards -e intra_cards.intra_cards -o dist/intra_cards
deactivate
rm -rf .build_env build
