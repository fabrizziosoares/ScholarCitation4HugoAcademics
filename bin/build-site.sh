#!/bin/sh

echo "Installing dependencies"
pip install six
pip install PyQuery

echo "Extracting Scholar data"
python bin/extractscholar.py OY4I82EAAAAJ

echo "Saving Scholar json on data folder"
mkdir -p data
mv citecount.json data/

echo "Calling hugo"
hugo
