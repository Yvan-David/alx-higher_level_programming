#!/usr/bin/node
function search () {
  let i, temp;
  let flag;
  const arr = [];
  for (let n = 2; n < process.argv.length; n++) {
    arr.push(parseInt(process.argv[n]));
  }
  for (i = 0; i < arr.length - 1; i++) {
    flag = 0;
    for (let j = 0; j < arr.length - 1; j++) {
      console.log(arr[j])
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        flag = 1;
      }
    }
    if (flag === 0) {
      break;
    }
  }
  console.log(arr)
}
if (process.argv.length <= 3) {
  console.log('0');
} else {
  search();
}
