let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let result = 0;

for (let i = parseInt(N / 5); i >= 0; i--) {
  let a = (N - 5 * i) / 3;
  if (Number.isInteger(a)) {
    result += i + a;
    break;
  }
}

if (result == 0) {
  result = -1;
}

console.log(result);
