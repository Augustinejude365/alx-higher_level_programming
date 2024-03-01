#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a
parameter, and finally displays the body of the response.
"""
import requests
from sys import argv


def post_emailreq():
    """
    sends a POST request to the passed URL with the email
    as a parameter
    """
    url = argv[1]
    values = {'email': argv[2]}
    req = requests.post(url, data=values)
    print(req.text)


if __name__ == "__main__":
    post_emailreq()
