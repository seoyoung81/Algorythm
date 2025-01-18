let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let S = Number(input[0]);
let result = 0;

for (let i = 1; i < S+1; i++) {
  if (S < ((1 + i) * i) / 2) {
    result = i;
    break;
  }
}
if (S == 1) result = 2;

console.log(result - 1);
