let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let time = input[1]
  .split(" ")
  .map(Number)
  .sort(function (a, b) {
    return a - b;
  });

let result = 0;
for (let i = 0; i < N; i++) {
  result += time[i] * (N - i);
}
console.log(result);
