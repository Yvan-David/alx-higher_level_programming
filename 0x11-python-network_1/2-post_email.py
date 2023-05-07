#!/usr/bin/python3
""" module that POST an email and display response body """

if __name__ == '__main__':
    import sys
    import urllib.request

    data = f'email={sys.argv[2]}'
    edata = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], edata)
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print(html.decode('utf8'))
