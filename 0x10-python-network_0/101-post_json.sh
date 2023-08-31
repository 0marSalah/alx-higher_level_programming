#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -sX -H "Content-Type: application/json" -d "$2" "$1"
