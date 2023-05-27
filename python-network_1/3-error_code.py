#!/usr/bin/python3
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

url = argv[1]

try:
    with urlopen(url) as response:
        r = response.read().decode('utf-8')
    print(r)
except HTTPError as e:
    print('Error code: ' + str(e.code))
