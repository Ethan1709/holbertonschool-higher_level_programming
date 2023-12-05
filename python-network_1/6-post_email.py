#!/usr/bin/python3
"""Comments"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    r = requests.post(url, data=data)
    print(r.text)
