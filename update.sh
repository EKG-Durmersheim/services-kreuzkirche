#!/bin/bash
for dir in ./services/*; do (cd "$dir" && docker compose pull && docker-compose down && docker-compose up -d); done
