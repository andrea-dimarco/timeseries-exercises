#!/bin/bash

script_dir=`dirname "$0"`

echo "Running containter for Time Series course ... "
docker run -it --volume "${script_dir}/app":"/app" \
               --volume "${script_dir}/data":"/data" \
               --name time_series_container DIMA/timeseries:latest \
                python /app/main.py


docker rm time_series_container &> /dev/null
echo "Container for Time Series course removed."
