#!/bin/bash

echo "Stoping and removing the application containers ..."
docker stop time_series_container
docker rm time_series_container

echo "Removing the appplication docker images ..."
docker rmi DIMA/timeseries:latest

echo "Done."