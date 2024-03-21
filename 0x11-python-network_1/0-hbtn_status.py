#!/usr/bin/python3
"""
This is a script that fetches https://alx-intranet.hbtn.io/status.
useing urlib package
"""


if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as reqs:
        content = reqs.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))