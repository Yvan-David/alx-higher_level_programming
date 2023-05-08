#!/usr/bin/python3
""" post url and email address """

import sys
import requests

if __name__ == '__main__':
    if sys.argv[2].find('=') != -1:
        load = sys.argv[2]
    else:
        load = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], load)
    print(r.text)
