#!/usr/bin/python3
from urllib.request import urlopen

with urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
print('Body response:')
print('\t- ' + 'type: ' + str(type(html)))
print('\t- ' + 'content: ' + str(html))
print('\t- ' + 'utf8 content: ' + str(html.decode('utf-8')))
