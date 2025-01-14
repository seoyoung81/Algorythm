let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let arr = input.map(Number);
let set_42 = new Set();

for (let i = 0; i < 10; i++) {
  set_42.add(arr[i] % 42);
}

console.log(set_42.size);
