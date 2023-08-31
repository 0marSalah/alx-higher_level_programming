#!/bin/bash
# get body only if status is ok
curl -s OPTIONS "$1"
