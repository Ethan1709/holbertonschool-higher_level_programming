#!/bin/bash
#Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -L -s -o /dev/null --write-out "%{http_code}" "$1"
