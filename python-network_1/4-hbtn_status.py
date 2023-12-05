#!/usr/bin/env python3
"""Comments"""

import requests

r = requests.get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t- ' + 'type: ' + str(type(r.text)))
print('\t- ' + 'content: ' + str(r.text))
