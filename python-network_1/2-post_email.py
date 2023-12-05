#!/usr/bin/python3
"""Python script that takes in a URL"""

from urllib.request import urlopen
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    value = {'email': email}
    data = parse.urlencode(value).encode()

    req = request.Request(url, data)
    with urlopen(req) as r:
        print(r.read().decode('utf-8'))
