let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = new Array();

for (let i = 1; i < n + 1; i++) {
  arr.push(input[i]);
}

function compare(a, b) {
  return a - b;
}

arr.sort(compare);

for (let j = 0; j < n; j++) {
  console.log(arr[j]);
}
