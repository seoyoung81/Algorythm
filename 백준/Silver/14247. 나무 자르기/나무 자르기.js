let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let h = input[1].split(" ").map(Number);
let a = input[2].split(" ").map(Number);

let arr = [];
for (let i = 0; i < n; i++) {
  arr.push([h[i], a[i]]);
}

arr.sort((a, b) => a[1] - b[1]);
let result = 0;
for (let i = 0; i < n; i++) {
  result += arr[i][0] + i * arr[i][1];
}
console.log(result);
