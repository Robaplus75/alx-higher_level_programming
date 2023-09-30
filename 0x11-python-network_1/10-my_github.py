#!/usr/bin/python3
"""
For displaying a GitHub ID based on given credentials.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    mrauth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    sssr = requests.get("https://api.github.com/user", auth=mrauth)
    print(sssr.json().get("id"))
