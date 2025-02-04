let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 0; i < n; i++) {
  arr.push(input[i + 1].split(" ").map(Number));
}

let dp = new Array(n).fill(0).map(() => new Array(3).fill(1e10));
dp[0] = arr[0];

for (let i = 1; i < n; i++) {
  // n 개의 집을 돌면서
  for (let j = 0; j < 3; j++) {
    // 지금 내가 j번째 색을 쓸건데
    for (let k = 0; k < 3; k++) {
      // i - 1번째 쓴 색 k랑 j는 같으면 안됨
      if (j != k) {
        dp[i][j] = Math.min(dp[i][j], dp[i - 1][k] + arr[i][j]);
      }
    }
  }
}

console.log(Math.min(...dp[n - 1]));
