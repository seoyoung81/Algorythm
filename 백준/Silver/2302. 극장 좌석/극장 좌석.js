let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]); // 좌석의 개수
let m = Number(input[1]); // 고정석의 개수
let arr = new Array(n + 1).fill(0);
for (let i = 0; i < m; i++) {
  let index = Number(input[i + 2]);
  arr[index] = 1;
}

let dp = new Array(n + 1).fill(1);
for (let i = 2; i < n + 1; i++) {
  if (arr[i] != 1 && arr[i - 1] != 1) dp[i] = dp[i - 1] + dp[i - 2];
  else dp[i] = dp[i - 1];
}

console.log(dp[n]);
