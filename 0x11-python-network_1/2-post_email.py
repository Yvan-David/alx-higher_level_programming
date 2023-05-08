#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8) """

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    email_dict = {"email": email}
    encode = urllib.parse.urlencode(email_dict)
    encode = encode.encode('ascii')
    request = urllib.request.Request(url, encode)

    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))
