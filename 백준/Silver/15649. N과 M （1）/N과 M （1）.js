let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [N, M] = input[0].split(" ").map(Number);
let arr = [];
for (let i = 1; i <= N; i++) arr.push(i);

let visited = new Array(0).fill(false); // 인덱스별 방문 여부
let selected = []; // 현재 순열에 포함된 원소

let answer = "";
function dfs(arr, depth) {
  if (depth == M) {
    let result = [];
    for (let i of selected) result.push(arr[i]);
    for (let j of result) answer += j + " ";
    answer += "\n";
    return;
  }

  for (let i = 0; i < arr.length; i++) {
    if (visited[i]) continue;
    visited[i] = true;
    selected.push(i);
    dfs(arr, depth + 1);
    visited[i] = false;
    selected.pop();
  }
}

dfs(arr, 0);
console.log(answer);
