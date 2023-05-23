#!/usr/bin/node
/* file that use request module to get a webpage */
const request = require('request');
request(process.argv[2], function (err, response) {
  if (err) {
    console.error(err);
  }
  console.log('code:', response.statusCode);
});
