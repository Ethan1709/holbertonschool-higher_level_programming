#!/usr/bin/python3
"""Python script that takes in a URL"""

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}

    with urlopen(url) as response:
        r = response.read().decode('utf-8')
    print('Your email is: ' + r)
