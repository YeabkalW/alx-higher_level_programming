#!/bin/bash
# a bash script that takes in a url, sends a GET request to the
# url. and displays the body of the response

# sends GET request and stores the response
res=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [["$res" == "200" ]]; then
    curl -s "$1"
fi
