#!/bin/bash
# script that sends a JSON POST request to a
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
