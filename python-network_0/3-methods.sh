#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -v -s -o /dev/null "$1" 2>&1 | grep -i allow | cut -d' ' -f2-
