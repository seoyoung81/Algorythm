let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let one = Number(input[1]);
let arr = [];

for (let i = 0; i < n - 1; i++) {
  arr.push(Number(input[i + 2]));
}

let maxV = Math.max(...arr);
let count = 0;
if (n == 1) console.log(0);
else {
  while (one <= maxV) {
    arr[arr.indexOf(maxV)] -= 1;
    one += 1;
    count++;
    maxV = Math.max(...arr);
  }
  console.log(count);
}
