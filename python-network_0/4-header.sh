#!/bin/bash
#Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s -X GET -d "X-HolbertonSchool-User-Id=98" "$1"
