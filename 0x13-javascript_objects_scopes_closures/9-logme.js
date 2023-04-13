#!/usr/bin/node
exports.logMe = function (item) {
  let count = -1;
  if (item) {
    count++;
  }
  console.log(count + ': ', item);
};
