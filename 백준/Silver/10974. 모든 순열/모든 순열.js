let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) arr.push(i);

let visited = new Array(n).fill(false);
let selected = []

let answer = "";
function dfs(arr, depth) {
  if (depth == n) {
    let result = [];
    for (let i of selected) result.push(arr[i])
    for (let j of result) answer += j + " "
    answer += "\n"
    return
  }
  
  for (let i = 0; i < n; i++) {
    if (visited[i]) continue;
    selected.push(i)
    visited[i] = true;
    dfs(arr, depth + 1)
    selected.pop()
    visited[i] = false;
  }
}

dfs(arr, 0)
console.log(answer)
