#!/bin/bash
# script that takes in a URL and displays
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-