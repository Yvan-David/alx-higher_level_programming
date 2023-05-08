#!/usr/bin/python3
""" module that POST an email and display response body
    and prints the body of the response in html
"""

if __name__ == '__main__':
    import sys
    import urllib.request
    if sys.argv[2].find('=') != -1:
        data = sys.argv[2]
    else:
        dat = {"email": sys.argv[2]}
        data = urllib.parse.urlencode(dat)
    edata = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], edata)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
