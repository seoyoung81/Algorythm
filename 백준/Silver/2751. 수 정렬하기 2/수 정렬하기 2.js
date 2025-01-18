let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = input.slice(1, n+1).map(Number);

arr.sort(function(a, b) {
  return a - b;
})

let answer = ''
for (let i = 0; i < n; i++) {
  answer += arr[i] + '\n'
}

console.log(answer);
