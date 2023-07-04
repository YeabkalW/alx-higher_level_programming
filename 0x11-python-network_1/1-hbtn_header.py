#!/usr/bin/python3
"""a script that takes in a url  sends a request to
the URL and display the value of the X-Request-Id"""

import sys
import urllib.request

if __name__ == "__main__":
    """handle the script not to be excuted when imported"""
    with urllib.request.urlopen(sys.argv[1]) as url:
        data = url.headers

    header = data.get("X-Request-id")
    print(header)
