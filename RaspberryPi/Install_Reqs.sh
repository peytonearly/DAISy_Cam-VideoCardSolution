#!/bin/bash

path=$PWD
pip install -y pipreqs
pipreqs $path
pip install -r requirements.txt