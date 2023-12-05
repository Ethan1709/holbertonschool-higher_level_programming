#!/usr/bin/python3
"""Comments"""

import requests
from sys import argv

url = argv[1]

r = requests.get(url)
print(r.headers.get('X-Request-Id'))
