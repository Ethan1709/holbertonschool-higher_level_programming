#!/bin/bash
#Bash script that takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -X DELETE -s "$1"
