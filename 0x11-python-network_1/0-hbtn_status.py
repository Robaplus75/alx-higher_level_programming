#!/usr/bin/python3
"""
For Fetching alx-intranet.hbtn.io/status.
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(request) as resp:
        body = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
