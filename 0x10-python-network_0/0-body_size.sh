#!/bin/bash
# a bash script that takes url and send request to display the
# the size of the body of the response.

curl -sI $1 | awk '/Content-Length/ (print $2)'
