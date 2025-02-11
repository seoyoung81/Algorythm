let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);
let m = Number(input[2]);

// 구간 합 구하기
let sumArr = [0, arr[0], ...new Array(n - 1).fill(0)];
for (let i = 2; i < n + 1; i++) {
  sumArr[i] = sumArr[i - 1] + arr[i - 1];
}

for (let i = 0; i < m; i++) {
  let [left, right] = input[i + 3].split(" ").map(Number);
  console.log(sumArr[right] - sumArr[left - 1]);
}
