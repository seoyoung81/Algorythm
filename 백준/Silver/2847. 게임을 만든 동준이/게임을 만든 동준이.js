let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 0; i < n; i++) {
  arr.push(Number(input[i + 1]));
}

let result = 0;
for (let i = n - 2; i >= 0; i--) {
  let a = arr[i] - arr[i + 1];
  if (a >= 0) {
    arr[i] = arr[i] - a - 1;
    result += a + 1;
  }
}

console.log(result);
