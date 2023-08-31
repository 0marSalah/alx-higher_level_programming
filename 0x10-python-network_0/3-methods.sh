#!/bin/bash
# get body only if status is ok
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
