#!/bin/bash

docker volume create sensordados 
docker build -t sensorapp:v1.0 . 
docker compose up -d 
sleep 15 
docker compose down
python3 dados/parser.py