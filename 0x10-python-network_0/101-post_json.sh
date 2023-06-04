#!/bin/bash
#post a json file
curl -H "Accept: application/json" -X POST -d @$2 $1
