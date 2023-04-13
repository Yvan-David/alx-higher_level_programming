#!/usr/bin/node
esrever = function (list) {
  arr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
}
module.exports = esrever;