#!/bin/bash
#post a json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
