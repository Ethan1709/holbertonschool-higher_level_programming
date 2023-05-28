#!/usr/bin/python3
import requests
from sys import argv


email = argv[2]
url = argv[1]
data = {'email': email}
r = requests.post(url, data=data)
print('Your email is: ' + r.text)