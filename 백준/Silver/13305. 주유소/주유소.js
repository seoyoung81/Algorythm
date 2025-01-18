let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

// 도시의 개수
let N = Number(input[0]);
// 도로의 길이
let distance = input[1].split(" ").map(Number);
// 리터당 가격
let cost = input[2]
  .split(" ")
  .map(Number);

// 항상 최솟값으로 사기
let result = distance[0] * cost[0];
let minCost = 10001;
for (let i = 1; i < N - 1; i++) {
  minCost = Math.min(minCost, cost[i]);
  result += distance[i] * minCost;
}

console.log(result);