let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
let x = Number(input[2]);
let result = 0;

for (let i = 0; i < n; i++) {
  let j = i + 1;
  while (j < n) {
    if (arr[i] + arr[j] == x) {
      result++;
      break;
    } else if (arr[i] + arr[j] < x) {
      j++;
    } else break;
  }
}
console.log(result);
