let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, m] = input[0].split(" ").map(Number);
let arr = [];
for (let i = 0; i < n; i++) {
  let numbers = input[i + 1].split(" ").map(Number);
  arr.push(numbers);
}

// 부분합 구하기
let prefixSum = [new Array(m).fill(0)];
for (let i = 0; i < n; i++) {
  let intervalPrefixSum = [0];
  let intervalPrefixSumValue = 0;
  for (let j = 0; j < m; j++) {
    intervalPrefixSumValue += arr[i][j];
    intervalPrefixSum.push(intervalPrefixSumValue);
  }
  prefixSum.push(intervalPrefixSum);
}

// result
let k = Number(input[n + 1]);
for (let l = 0; l < k; l++) {
  let result = 0;
  let [i, j, x, y] = input[n + 2 + l].split(" ").map(Number);
  for (let p = i; p < x + 1; p++) {
    result += prefixSum[p][y] - prefixSum[p][j - 1];
  }
  console.log(result);
}
