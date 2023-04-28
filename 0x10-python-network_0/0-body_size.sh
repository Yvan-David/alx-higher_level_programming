#!/usr/bin/env bash
# a script that takes the url and display some of its messages

curl -i $1 -o saved
cat saves | grep Content-Length | cut -d ' ' -f 2