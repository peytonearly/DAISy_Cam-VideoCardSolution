#!/bin/bash

# This script finds and installs required Python libraries

path=$PWD
pip install -y pipreqs
pipreqs $path
pip install -r requirements.txt