#!/usr/bin/python3
""" module that POST an email and display response body
    and prints the body of the response in html
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    dat = {"email": argv[2]}
    data = urllib.parse.urlencode(dat)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
