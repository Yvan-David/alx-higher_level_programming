#!/bin/bash
# a script that takes the url and display some of its messages

curl -s "$1" | wc -c