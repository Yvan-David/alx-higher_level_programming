#!/usr/bin/node
function search () {
  let i, temp;
  for (i = 0; i < process.argv.length - 1; i++) {
    for (let j = 0; j < process.argv.length - 1; j++) {
      if (process.argv[j] > process.argv[j + 1]) {
        temp = process.argv[j];
        process.argv[j] = process.argv[j + 1];
        process.argv[j + 1] = temp;
      }
    }
  }
  console.log(process.argv[process.argv.length - 2]);
}
if (process.argv.length <= 3) {
  console.log('0');
} else {
  search();
}
