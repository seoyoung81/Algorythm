let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [k, n] = input[0].split(" ").map(Number); // 랜선 개수, 필요한 랜선 개수
let arr = [];

for (let i = 1; i < k + 1; i++) {
  arr.push(Number(input[i]));
}

let start = 1;
let end = arr.reduce((a, b) => Math.max(a, b));

let result = 0;
while (start <= end) {
  let total = 0;
  let mid = parseInt((start + end) / 2);

  for (x of arr) {
    total += parseInt(x / mid);
  }

  if (total >= n) {
    result = mid;
    start = mid + 1;
  } else end = mid - 1;
}

console.log(result);
