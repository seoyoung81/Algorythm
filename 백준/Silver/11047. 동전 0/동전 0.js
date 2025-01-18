let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [N, K] = input[0].split(" ").map(Number);
let coin = input.slice(1, N + 1).map(Number);

let result = 0;
for (let i = N - 1; i >= 0; i--) {
  result += parseInt(K / coin[i]);
  K = K % coin[i];
}

console.log(result);
