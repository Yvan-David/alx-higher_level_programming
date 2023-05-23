#!/usr/bin/node
/* writing to a file */
const file = require('fs');
file.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});
