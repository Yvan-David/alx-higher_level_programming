#!/usr/bin/node
function factorial (n) {
  let result = 1;
  if (n > 1) {
    result *= n * factorial(n - 1);
  }
  return (result);
}
console.log(factorial(parseInt(process.argv[2])));
