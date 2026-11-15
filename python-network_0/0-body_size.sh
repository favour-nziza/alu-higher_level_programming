#!/bin/bash
# Displays the size of the body of the response of a request to a URL
curl -s "$1" | wc -c
