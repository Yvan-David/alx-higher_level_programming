#!/bin/bash
# print allowed methods
curl -si $1 -o nom; cat nom | grep Allow: | cut -d ' ' -f 2-
