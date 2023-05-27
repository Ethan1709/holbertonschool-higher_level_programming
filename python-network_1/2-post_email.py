#!/usr/bin/python3
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


email = argv[2]
url = argv[1]
data = {'email': email}

with urlopen(url) as response:
    r = response.read().decode('utf-8')
print('Your email is: ' + r)