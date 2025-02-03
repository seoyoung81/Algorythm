let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [0];
for (let i = 1; i < n + 1; i++) arr.push(Number(input[i]));

let dp = new Array(n + 1).fill(0);
dp[1] = arr[1];
dp[2] = arr[1] + arr[2];
for (let i = 3; i < n + 1; i++) {
  dp[i] = Math.max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3]);
  dp[i] = Math.max(dp[i], dp[i - 1]);
}
console.log(dp[n]);
