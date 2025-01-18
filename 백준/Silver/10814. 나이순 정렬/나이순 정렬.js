let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let arr = [];

for (let i = 1; i < N + 1; i++) {
  let [age, name] = input[i].split(" ");
  arr.push([Number(age), name]);
}

function compare(a, b) {
  if (a[0] != b[0]) return a[0] - b[0];
}

arr.sort(compare);

let result = "";
for (let char of arr) {
  result += char[0] + " " + char[1] + "\n";
}

console.log(result);
