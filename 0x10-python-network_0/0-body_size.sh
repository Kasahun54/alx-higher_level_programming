#!/bin/bash
#takes the URL, and sends a request to that URL
curl -s "$1" | wc -c
