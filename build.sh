#!/bin/bash

script_dir=`dirname "$0"`

echo "Building the image for Time Series course ... "
docker build -t DIMA/timeseries:latest .