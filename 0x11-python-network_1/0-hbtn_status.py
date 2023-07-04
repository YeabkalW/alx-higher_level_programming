#!/usr/bin/python3
"""
a python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

link = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    '''handls the script not to be excuted when runned'''
    with urllib.request.urlopen(link) as response:
        """opens the url and reads the data"""
        data = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf-8')))
