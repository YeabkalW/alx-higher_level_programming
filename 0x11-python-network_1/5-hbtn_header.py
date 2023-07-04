#!/usr/bin/python3
"""displayes the header variable of a request"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    request_id = response.headers.get("X-Request_ID")
    print(request_id)
