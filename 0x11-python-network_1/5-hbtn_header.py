#!/usr/bin/python3
"""
For ouputing the X-Request-Id header variable of a
request to a given URL
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    sr = requests.get(url)
    print(sr.headers.get("X-Request-Id"))
