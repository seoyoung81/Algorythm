let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split("\n");

number1 = Number(input[0])
number2_split = input[1].split('').map(Number)
number2 = Number(input[1])

for (let num of number2_split.reverse()) {
  console.log(number1 * num);
}

console.log(number1*number2)