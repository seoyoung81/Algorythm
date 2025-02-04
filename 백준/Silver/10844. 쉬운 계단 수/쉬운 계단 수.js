let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let dp = Array.from(Array(n + 1), () => new Array(10).fill(0));

for (let i = 1; i < 10; i++) {
  dp[1][i] = 1;
}

for (let i = 2; i <= n; i++) {
  for (let j = 0; j <= 9; j++) {
    if (j > 0) dp[i][j] += dp[i - 1][j - 1];
    if (j < 9) dp[i][j] += dp[i - 1][j + 1];
    dp[i][j] %= Number(1e9);
  }
}

let result = 0;
for (let j = 0; j <= 9; j++) {
  result += dp[n][j];
  result %= Number(1e9);
}

console.log(result);
