let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, m] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number);
let result = 0;

for (let i = 0; i < n; i++) {
  let intervalSum = 0;
  let j = i;
  while (j < n) {
    intervalSum += arr[j];
    j++;
    if (intervalSum == m) {
      result++;
    } else if (intervalSum > m) break;
  }
}
console.log(result);
