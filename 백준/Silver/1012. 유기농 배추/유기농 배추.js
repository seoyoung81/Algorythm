let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

function dfs(graph, n, m, x, y) {
  if (x <= 0 || x > n || y <= 0 || y > m) return false;
  if (graph[x][y] == 1) {
    // 방문 처리
    graph[x][y] = 2;

    // 상하좌우
    dfs(graph, n, m, x + 1, y);
    dfs(graph, n, m, x - 1, y);
    dfs(graph, n, m, x, y + 1);
    dfs(graph, n, m, x, y - 1);

    return true;
  }
  return false;
}

let T = Number(input[0]);
let line = 1;
for (let i = 0; i < T; i++) {
  let [m, n, k] = input[line].split(" ").map(Number);
  let arr = new Array(n + 1).fill(0).map(() => new Array(m + 1).fill(0));

  for (let i = 0; i < k; i++) {
    let [x, y] = input[line + i + 1].split(" ").map(Number);
    arr[y + 1][x + 1] = 1;
  }

  let answer = 0;

  // dfs 탐색
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      if (dfs(arr, n, m, i, j)) answer++;
    }
  }
  line += k + 1;
  console.log(answer);
}
