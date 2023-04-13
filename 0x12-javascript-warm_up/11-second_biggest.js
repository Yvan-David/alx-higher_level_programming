#!/usr/bin/node
function search () {
  let i;
  let v = 0;
  const arr = [];
  for (i = 2; i <= process.argv.length; i++) {
    if (parseInt(process.argv[i]) < 0) {
      v = parseInt(process.argv[i]);
    }
  }
  for (i = 2; i <= process.argv.length; i++) {
    if (parseInt(process.argv[i]) > v) {
      v = parseInt(process.argv[i]);
      console.log(v);
      arr.push(v);
    }
  }
  console.log(arr[arr.length - 2]);
}
if (process.argv.length <= 3) {
  console.log('0');
} else {
  search();
}
