#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -s -o /dev/null -w "%{http_code}" "$1"
