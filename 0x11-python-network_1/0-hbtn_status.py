#!/usr/bin/python3
""" module that request url and reads content in bytes and html """
if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status")\
         as response:
        html = response.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf8')}")
