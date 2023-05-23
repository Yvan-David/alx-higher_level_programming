#!/usr/bin/node
/* a script that use api to get content from web */
const url = process.argv[2];
const request = require('request');
request({ url, json: true }, function (err, response) {
  if (err) {
    console.error(err);
  } else {
    console.log(response.body.results.characters);
  }
});
