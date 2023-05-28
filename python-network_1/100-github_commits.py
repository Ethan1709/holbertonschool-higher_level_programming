#!/usr/bin/python3
import requests
from sys import argv, exit

repo = argv[1]
owner_name = argv[2]
count = 0

try:
    r = requests.get('https://api.github.com/repos/rails/rails/commits', auth=(repo, owner_name))
    repo_data = r.json()
    for i in repo_data:
        sha_val = (i.get('sha'))
        j = (i.get('commit'))
        l = (j['author'])
        print(str(sha_val) + ': ' + str(l.get('name')))
except requests.exceptions.RequestException:
    exit(1)