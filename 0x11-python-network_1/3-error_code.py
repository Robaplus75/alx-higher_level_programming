#!/usr/bin/python3
"""
For sending request to a given URL
And For ouputing the response body.
"""
import urllib.error
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as resp:
            print(resp.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
