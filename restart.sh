#!/bin/bash
for dir in ./services/*; do (cd "$dir" && docker-compose down && docker-compose up -d); done
