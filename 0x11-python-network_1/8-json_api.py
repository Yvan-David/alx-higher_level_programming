#!/usr/bin/python3
""" takes in a letter and sends a POST request to
to use json file of the response """

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    load = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, load)

    try:
        json_dict = r.json()
        if json_dict:
            print(f"{[json_dict.get('id')]} {json_dict.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")