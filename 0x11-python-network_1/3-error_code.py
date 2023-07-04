#!/usr/bin/python3
"""
a python scrpt that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in
utf-8)
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urlib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as f:
        print("Error code: {}".format(f.code))
