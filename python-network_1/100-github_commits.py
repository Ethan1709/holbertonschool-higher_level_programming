#!/usr/bin/python3
"""Comments"""

import requests
from sys import argv

if __name__ == "__main__":
    rails1 = argv[1]
    rails2 = argv[2]
    url = f'https://api.github.com/repos/{rails1}/{rails2}/commits'

    r = requests.get(url)
    repo_data = r.json()
    try:
        for i in repo_data:
            commit_sha = i.get("sha")
            author = i.get("commit").get("author").get("name")
            print(f'{commit_sha}: {author}')
    except IndexError:
        pass
