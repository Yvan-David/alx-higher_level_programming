#!/bin/bash
# using dev/null and -w to display status code
curl -s -o dev/null -w "%{http_code}" $1
