#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
