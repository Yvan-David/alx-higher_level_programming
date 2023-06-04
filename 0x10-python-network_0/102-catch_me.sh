#!/bin/bash
#sending a request and displaying  a text
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
