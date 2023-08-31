#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
