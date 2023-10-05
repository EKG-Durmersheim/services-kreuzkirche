#!/bin/bash
for dir in ./services/*; do (cd "$dir" && docker-compose up -d); done