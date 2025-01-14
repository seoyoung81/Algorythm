let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split("\n");

let [a, b, c] = input[0].split(" ").map(Number).sort();

// 같은 눈 3개
if (a == b && a == c) {
  console.log(10000 + a * 1000);
} else if (a == b || a == c) {
  // 같은 눈이 2개
  console.log(1000 + a * 100);
} else if (b == c) {
  console.log(1000 + b * 100);
} else {
  console.log(c * 100);
}
