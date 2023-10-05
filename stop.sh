#!/bin/bash
for dir in ./services/*; do (cd "$dir" && docker-compose down); done