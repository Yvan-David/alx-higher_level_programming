#!/usr/bin/python3
""" module that recieves a response """

import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.headers['X-Request-Id']:
        print((r.headers.get('X-Request-Id')))
