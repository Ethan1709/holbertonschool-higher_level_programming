#!/usr/bin/python3
from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as response:
    headers = response.getheaders()
for i in headers:
    if i[0] == 'X-Request-Id':
        print(i[1])