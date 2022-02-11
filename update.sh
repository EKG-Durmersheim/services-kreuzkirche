#!/bin/sh
docker-compose down
git pull
chown docker-runner:docker-runner -R *
docker-compose up -d