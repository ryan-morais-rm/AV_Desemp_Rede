#!/bin/bash

docker volume create cameradados
docker build -t cameraapp:v1.0
docker compose up -d
sleep 40
docker compose down