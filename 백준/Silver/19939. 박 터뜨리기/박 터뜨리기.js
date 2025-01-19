let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [N, K] = input[0].split(" ").map(Number);
for (let i = 1; i < K + 1; i++) {
  N -= i;
}

if (N < 0) {
  console.log(-1);
} else if (N % K === 0) {
  console.log(K - 1);
} else console.log(K);
