let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let dp = new Array(101).fill(0);
dp[1] = dp[2] = dp[3] = 1;
dp[4] = dp[5] = 2;
for (let i = 6; i < 101; i++) {
  dp[i] = dp[i - 1] + dp[i - 5];
}

let T = Number(input[0]);
for (let tc = 0; tc < T; tc++) {
  let n = Number(input[tc + 1]);
  console.log(dp[n]);
}
