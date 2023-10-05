#!/bin/bash
for dir in ./*; do (cd "$dir" && docker-compose down && docker-compose up -d); done
