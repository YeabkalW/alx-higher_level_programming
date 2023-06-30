#!/bin/bash
# a bash script that takes in a url and displays all HTTP
# methods the server will accept

curl -s -I $1 | grep -i Allow
