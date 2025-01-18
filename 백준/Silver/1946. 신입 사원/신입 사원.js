let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let T = Number(input[0]);
let line = 1;
for (let tc = 0; tc < T; tc++) {
  let N = Number(input[line]);
  let arr = [];
  for (let i = line + 1; i < line + N + 1; i++) {
    arr.push(input[i].split(" ").map(Number));
  }

  arr.sort(function (a, b) {
    return a[0] - b[0];
  });

  let result = 1;

  let a = arr[0][1];
  for (let j = 1; j < arr.length; j++) {
    if (a > arr[j][1]) {
      result += 1;
      a = arr[j][1];
    }
  }

  console.log(result);
  line += N + 1;
}
