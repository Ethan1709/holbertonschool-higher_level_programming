#!/usr/bin/python3
""" Comments """

from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as response:
    """ Comments """
    x_request_id = response.headers.get('X-Request-Id')
print (x_request_id)
