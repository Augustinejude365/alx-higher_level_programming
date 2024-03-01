#!/usr/bin/python3
"""
A Python script that fetches an URL with requests package:
https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    reqs = requests.get('https://alx-intranet.hbtn.io/status')
    t = reqs.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
