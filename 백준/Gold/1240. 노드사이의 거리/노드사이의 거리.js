let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, m] = input[0].split(" ").map(Number);
let arr = new Array(n + 1).fill(null).map(() => []);

for (let i = 1; i < n; i++) {
  let [x, y, z] = input[i].split(" ").map(Number);
  arr[x].push([y, z]);
  arr[y].push([x, z]);
}

function dfs(x, dist) {
  if (visited[x]) return;
  // 방문 처리
  visited[x] = true;
  distance[x] = dist;
  for (let [y, z] of arr[x]) dfs(y, dist + z);
}

// result
for (let i = 0; i < m; i++) {
  let [x, y] = input[n + i].split(" ").map(Number);
  visited = new Array(n + 1).fill(false);
  distance = new Array(n + 1).fill(-1);
  dfs(x, 0);
  console.log(distance[y]);
}
