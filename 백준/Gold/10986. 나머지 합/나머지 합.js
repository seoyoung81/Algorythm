let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, m] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number);

// 구간 합 구하기
let prefixSum = [0];
let sumValue = 0;
for (let i = 0; i < n; i++) {
  sumValue += arr[i];
  prefixSum.push(sumValue);
}

let rest = new Array(n).fill(0);
for (let i = 1; i < n + 1; i++) {
  let r = prefixSum[i] % m;
  rest[r] += 1;
}

// 결과 구하기
let result = 0;
for (let i = 0; i < n; i++) {
  result += parseInt((rest[i] * (rest[i] - 1)) / 2);
}

console.log(result + rest[0]);
