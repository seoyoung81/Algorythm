let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, m] = input[0].split(" ").map(Number); // 나무의 수, 필요한 나무의 길이
let arr = input[1].split(" ").map(Number); // 나무의 높이

let start = 1;
let end = arr.reduce((a, b) => Math.max(a, b));

let result = 0;
while (start <= end) {
  let total = 0;
  let mid = parseInt((start + end) / 2);

  for (x of arr) {
    if (x - mid >= 0) total += x - mid;
  }

  if (total >= m) {
    result = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(result);
