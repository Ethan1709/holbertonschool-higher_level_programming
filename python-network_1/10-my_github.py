#!/usr/bin/env python3
"""Comments"""

import requests
from sys import argv, exit
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
