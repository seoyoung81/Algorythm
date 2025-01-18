let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let arr = [];

for (let i = 1; i < N + 1; i++) {
  arr.push(input[i].split(" ").map(Number));
}

arr.sort(function (a, b) {
  if (a[0] != b[0]) return a[0] - b[0];
  else return a[1] - b[1];
});

let answer = "";

for (let data of arr) {
  answer += data[0] + " " + data[1] + "\n";
}

console.log(answer);
