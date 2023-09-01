#!/usr/bin/python3
"""
script to get first 10 commits of a repo
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2])
    r = requests.get(url)
    for idx, i in enumerate(r.json()):
        if idx < 10:
            print("{}: {}".format(i.get('sha'), i.get(
                'commit').get('author').get('name')))
