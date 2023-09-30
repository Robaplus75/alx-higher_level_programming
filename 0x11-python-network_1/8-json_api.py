#!/usr/bin/python3
"""For Sending a POST request to 0.0.0.0:5000/search_user
with letter
"""
import requests
import sys


if __name__ == "__main__":
    # executes if run directly not while imported
    words = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": words}
    sr = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = sr.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
