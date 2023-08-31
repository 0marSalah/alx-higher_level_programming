#!/bin/bash
# get body only if status 200
echo "POST params:" "\n" "$(curl -s -X POST -d "email='test@gmail.com'&subject='I will always be here for PLD'" "$1")"
