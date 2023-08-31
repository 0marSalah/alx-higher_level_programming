#!/bin/bash
# get body only if status 200
email="test@gmail.com"
subject="I will always be here for PLD"
curl -X POST "$email $subject" "$1"
