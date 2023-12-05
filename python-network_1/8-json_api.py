#!/usr/bin/python3
"""Comments"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        data = {'q': argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', data)
        json_response = r.json()
        json_id = json_response['id']
        json_name = json_response['name']
        print(f'[{json_id}] {json_name}')
    except ValueError:
        print('Not a valid JSON')
    except IndexError:
        print('No result')
