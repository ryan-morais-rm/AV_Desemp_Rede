#!/bin/bash

docker volume create semaforodados 
docker build -t semaforoapp:v1.0 . 
docker compose up -d 
sleep 30
docker compose down
