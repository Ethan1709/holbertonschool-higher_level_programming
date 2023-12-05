#!/usr/bin/python3
"Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response."

from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as response:
    x_request_id = response.headers.get('X-Request-Id')
print (x_request_id)
