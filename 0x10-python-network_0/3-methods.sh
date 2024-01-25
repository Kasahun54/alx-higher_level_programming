#!/bin/bash
# take the URL and displays all HTTP methods the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
