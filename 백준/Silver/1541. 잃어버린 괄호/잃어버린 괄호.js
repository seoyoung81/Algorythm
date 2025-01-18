let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let arr = input[0].split("-");
let plus_lst = [];

for (let a of arr) {
  let sumValue = a
    .split("+")
    .map(Number)
    .reduce((a, b) => a + b);
  plus_lst.push(sumValue);
}

let result = 0;
for (let num of plus_lst) {
  result -= num;
}
console.log(result + plus_lst[0] * 2);
