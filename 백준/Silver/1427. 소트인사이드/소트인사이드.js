let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let arr = input[0].split("").map(Number);
arr.sort(function (a, b) {
  return b - a;
});

let result = "";
for (let char of arr) {
  result += char;
}

console.log(result);
