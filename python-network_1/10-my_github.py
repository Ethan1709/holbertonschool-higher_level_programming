#!/usr/bin/python3
"""Comments"""

import requests
from sys import argv, exit

if __name__ == "__main__":
    username = argv[1]
    token = argv[2]

    try:
        r = requests.get('https://api.github.com/users/Ethan1709', auth=(username, token))
        user_data = r.json()
        user_id = user_data['id']
        print(user_id)
    except requests.exceptions.RequestException:
        exit(1)
