#!/bin/bash
# a script that takes the url and display some of its messages
curl -is $1 -o saved | cat saved | grep Content-Length | cut -d ' ' -f 2
