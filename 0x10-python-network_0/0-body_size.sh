#!/bin/bash
# a bash script that takes url and send request to display the
# the size of the body of the response.
url="$1"

# Send request using curl, retrieve only the headers, and store in a variable
headers=$(curl -sI "$url")

# Extract the Content-Length header value
content_length=$(echo "$headers" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')

# Display the size of the body in bytes
echo "$content_length"
