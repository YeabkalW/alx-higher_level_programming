#!/usr/bin/python3
"""sends a request to a given URL, then displays the 
response body"""

import sys 
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    respo = requests.get(url)
    if respo.status_code >= 400:
        print("Error code: {}".format(respo.status_code))
    else:
        print(respo.text)
