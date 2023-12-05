#!/usr/bin/python3
"""Comments"""

import requests
from sys import argv, exit

if __name__ == "__main__":
    url = argv[1]

    try:
        r = requests.get(url)
        if r.status_code == 200 or r.status_code < 400:
            print(r.text)
        else:
            print('Error code:', r.status_code)
    except requests.exceptions.RequestException as e:
        exit(1)
