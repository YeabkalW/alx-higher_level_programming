#!/usr/bin/python3
"""Sends s Post request to a given URL"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data - {"email": email}

    respo = request.post(url, data=data)
    print(respo.text)
