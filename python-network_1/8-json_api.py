#!/usr/bin/python3
import requests
from sys import argv

data = {'q': argv[1]}

try:
    r = requests.post('https://chat.openai.com/', data=data)
    j = r.json()
    json_id = j['id']
    json_name = j['name']
    print(f'[{json_id}], {json_name}')
except ValueError:
    print('Not a valid JSON')