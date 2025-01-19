let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

// 회의의 수
let N = Number(input[0]);
// 회의의 정보
let arr = [];
for (let i = 1; i < N + 1; i++) {
  let [x, y] = input[i].split(" ").map(Number);
  arr.push([x, y]);
}

function compare(a, b) {
  if (a[1] != b[1]) {
    return a[1] - b[1];
  } else return a[0] - b[0];
}
arr.sort(compare);

let cnt = 1,
  cur = 0;
for (let i = 1; i < N; i++) {
  if (arr[cur][1] <= arr[i][0]) {
    cur = i;
    cnt += 1;
  }
}

console.log(cnt);
