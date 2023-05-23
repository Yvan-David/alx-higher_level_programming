#!/usr/bin/node
/* gets an api and prints user id and task completed */
const request = require('request');
const url = process.argv[2];
const dict = {};
request({ url, json: true }, function (err, response) {
  if (err) {
    console.error(err);
  } else {
    for (let i = 1; i < response.body.length - 1; i++) {
      if (response.body[i].completed === true) {
        dict[response.body[i].id] = response.body[i].userId;
      }
    }
    for (const key in dict) {
      console.log("'" + key + "'" + ': ' + dict[key] + ',');
    }
  }
});
