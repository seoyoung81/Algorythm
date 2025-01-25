let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [[0]];
for (let i = 0; i < n; i++) {
  arr.push([0, ...input[i + 1].split(" ").map(Number)]);
}

let visited = new Array(n + 1).fill(0);
let result = [];
let minValue = 1e9;

function dfs(depth) {
  if (depth == n - 1) {
    let cur = 1;
    let totalCost = 0;
    for (let i = 0; i < n - 1; i++) {
      let nextNode = result[i];
      let cost = arr[cur][nextNode];
      if (cost == 0) return;
      totalCost += cost;
      cur = nextNode;
    }
    // 마지막 도시에서 돌아오기
    let cost = arr[cur][1];
    if (cost == 0) return;
    totalCost += cost;
    minValue = Math.min(totalCost, minValue);
  }

  for (let i = 2; i <= n; i++) {
    if (visited[i]) continue;
    result.push(i);
    visited[i] = true;
    dfs(depth + 1);
    result.pop();
    visited[i] = false;
  }
}

dfs(0);
console.log(minValue);
