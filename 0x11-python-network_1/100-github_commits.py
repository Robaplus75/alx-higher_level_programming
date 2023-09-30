#!/usr/bin/python3
"""
For Listing the 10 most recent commits on a given GitHub repo
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    sssr = requests.get(url)
    commited = sssr.json()
    try:
        for k in range(10):
            print("{}: {}".format(
                commited[k].get("sha"),
                commited[k].get("commit").get("author").get("name")))
    except IndexError:
        pass
