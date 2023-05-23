#!/usr/bin/node
/* file that recieves file path and reads the file */
const file = require('fs');
file.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
