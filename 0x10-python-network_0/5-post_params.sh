#!/bin/bash
# get body only if status 200
url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

echo "POST params:"
echo "$response"
