#!/usr/bin/node
/* get a request and write into a file */
const request = require('request');
const url = process.argv[2];
request({ url, json: true }, function (err, response) {
  if (err) {
    console.error('error 1:', err);
  } else {
    const file = require('fs');
    file.writeFile(process.argv[3], response.body, function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
