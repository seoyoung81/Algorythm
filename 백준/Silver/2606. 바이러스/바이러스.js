let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]); // 컴퓨터의 수 -> 노드의 수
let m = Number(input[1]); // 직접 연결되어 있는 컴퓨터 쌍의 수 -> 간선의 수
let computers = new Array(n + 1).fill(null).map(() => []);

for (let i = 0; i < m; i++) {
  let [x, y] = input[i + 2].split(" ").map(Number);
  computers[x].push(y);
  computers[y].push(x);
}

function dfs(arr, v, visited) {
  // 현재 노드 방문 처리
  visited[v] = 1;
  result += 1;
  // 재귀
  for (let i of arr[v]) {
    if (!visited[i]) {
      dfs(arr, i, visited);
    }
  }
}

let visited = new Array(n + 1).fill(false);
let result = 0;
dfs(computers, 1, visited);

console.log(result - 1);
