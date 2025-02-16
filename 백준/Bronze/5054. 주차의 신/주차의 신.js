let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let t = Number(input[0]);
let line = 1;
for (let tc = 0; tc < t; tc++) {
  let n = Number(input[tc + line]);
  let location = input[tc + line + 1]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  console.log((location[n - 1] - location[0]) * 2);
  line += 1;
}
