let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let T = Number(input[0]);
let result = "";

for (let i = 0; i < T; i++) {
  let [a, b] = input[i + 1].split(" ");
  for (let j = 0; j < b.length; j++) {
    for (let k = 0; k < a; k++) result += b[j];
  }
  result += "\n";
}

console.log(result);
