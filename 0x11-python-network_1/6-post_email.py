#!/usr/bin/python3
"""
For Sending  a POST request to a given URL
with a given email.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    sr = requests.post(url, data=value)
    print(sr.text)
