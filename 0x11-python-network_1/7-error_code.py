#!/usr/bin/python3
"""
For sending request to a given URL
displays the response body.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    sr = requests.get(url)
    if sr.status_code >= 400:
        print("Error code: {}".format(sr.status_code))
    else:
        print(sr.text)
