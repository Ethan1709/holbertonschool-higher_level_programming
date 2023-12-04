#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
url="$1"
body=$(curl -s -w "%{http_code}" "$url")
http_status="${body: -3}"

if  [ "$http_status" == 200 ]; then
    echo "$body"
else
    echo ""
fi
