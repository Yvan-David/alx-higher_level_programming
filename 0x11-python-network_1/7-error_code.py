#!/usr/bin/python3
""" module that handles http error codes """

import sys
import requests

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    code = r.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(r.text)
