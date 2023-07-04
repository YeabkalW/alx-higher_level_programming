#!/usr/bin/python3
"""a python script that takes in a URl
and an email, sends a POST request to
the passed URL with the email as a
Parameter, and displays the body of the
response in UTF-8 decoding
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    """handles the script from being excuted"""
    paramet = urllib.parse.urlencode({'email': sys.argv[2]})
    paramet = paramet.encode("utf-8")

    header = {"Content-Type": 'application/x-www-form-urlencoded'}

    request = urllib.request.Request(sys.argv[1], data=paramet, headers=header)

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
