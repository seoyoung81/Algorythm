let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = new Array(1).fill(null).map(() => new Array(n + 1).fill(0));
for (let i = 0; i < n; i++) {
  let home = input[i + 1].split("").map(Number);
  arr.push([0, ...home]);
}

function dfs(arr, n, i, j) {
  // 범위 제한
  if (i <= 0 || i > n || j <= 0 || j > n) return 0;
  if (arr[i][j] == 1) {
    // 방문 처리
    arr[i][j] = 2;
    let size = 1;

    // 상하좌우
    size += dfs(arr, n, i, j + 1);
    size += dfs(arr, n, i, j - 1);
    size += dfs(arr, n, i + 1, j);
    size += dfs(arr, n, i - 1, j);

    return size;
  }
   return 0;
}

let answer = 0;
let result = [];

// dfs
for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= n; j++) {
    let size = dfs(arr, n, i, j);
    if (size > 0) {
      answer++;
      result.push(size);
    }
  }
}

console.log(answer);

result.sort((a, b) => a - b);
for (let i = 0; i < result.length; i++) console.log(result[i]);
