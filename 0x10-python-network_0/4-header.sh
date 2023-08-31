#!/bin/bash
# get body only if status is ok
curl -s -H "X-School-User-Id: 98" GET "$1"
