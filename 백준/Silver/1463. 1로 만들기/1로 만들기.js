let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let dp = new Array(n + 1).fill(1);
dp[1] = 0;

for (let i = 4; i < n + 1; i++) {
  // 1 빼는 경우는 매번 한다.
  dp[i] = dp[i - 1] + 1;

  if (i % 2 == 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);
  if (i % 3 == 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);
}

console.log(dp[n]);
