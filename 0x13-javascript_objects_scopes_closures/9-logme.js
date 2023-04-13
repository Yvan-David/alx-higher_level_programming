#!/usr/bin/node
count = -1;
logMe = function (item) {
  if(item) {
    count++;
  }
  console.log(count + ": ",item);
}
module.exports = logMe;
