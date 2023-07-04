#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given char.
"""
import sys
import requests


if __name__ == "__main__":
    char = "" if len(sys.argv) == 1 else sys.argv[1]
    load = {"q": char}

    req = requests.post("http://0.0.0.0:5000/search_user", data=load)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
