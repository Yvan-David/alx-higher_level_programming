#!/usr/bin/python3
""" module that POST an email and display response body """

if __name__ == '__main__':
    try:
        import sys
        import urllib.request
        if sys.argv[2].find('=') != -1:
            data = sys.argv[2]
        else:
            data = f'email={sys.argv[2]}'
        edata = data.encode('ascii')
        req = urllib.request.Request(sys.argv[1], edata)
        with urllib.request.urlopen(req) as response:
            html = response.read()
        print(html.decode('utf8'))
    except IndexError:
        print('please check arguments parsed')
