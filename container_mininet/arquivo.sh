#!/bin/bash

# Criação das redes privadas com blocos definidos.
docker network create -d bridge --subnet=172.19.0.0/16 brteste02
docker network create -d bridge --subnet=172.18.0.0/16 brteste01

# Rodando os containers client e server.
docker run --name server --network brteste02 --ip 172.19.0.2 –cap-add=NET_ADMIN -dit image_ubuntu:latest
docker run --name client --network brteste01 --ip 172.18.0.2 –cap-add=NET_ADMIN -dit image_ubuntu:latest

# Adicionando rotas, server e client, respectivamente.
ip route add 172.18.0.0/16 via 172.19.0.10
ip route add 172.19.0.0/16 via 172.18.0.10
