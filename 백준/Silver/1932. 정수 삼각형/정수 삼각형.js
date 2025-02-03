let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i < n + 1; i++) {
  arr.push(input[i].split(" ").map(Number));
}

let dp = [];
for (let i = 1; i < n + 1; i++) {
  let zero = new Array(i).fill(0);
  dp.push(zero);
}

if (n == 1) console.log(arr[0][0]);
else if (n == 2) console.log(Math.max(arr[1][0], arr[1][1]) + arr[0][0]);
else {
  dp[0][0] = arr[0][0];
  dp[1][0] = dp[0][0] + arr[1][0];
  dp[1][1] = dp[0][0] + arr[1][1];

  for (let i = 2; i < n; i++) {
    for (let j = 0; j < i + 1; j++) {
      if (j == 0) dp[i][j] = dp[i - 1][j] + arr[i][j];
      else if (j == i) dp[i][j] = dp[i - 1][j - 1] + arr[i][j];
      else
        dp[i][j] = Math.max(
          dp[i - 1][j - 1] + arr[i][j],
          dp[i - 1][j] + arr[i][j]
        );
    }
  }

  let result = dp[n - 1];
  console.log(result.reduce((a, b) => Math.max(a, b)));
}
