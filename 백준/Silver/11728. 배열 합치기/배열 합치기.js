let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, m] = input[0].split(" ").map(Number);
let arrA = [...input[1].split(" ").map(Number), 1e9];
let arrB = [...input[2].split(" ").map(Number), 1e9];
let result = "";

let indexA = 0;
let indexB = 0;
while (indexA < n || indexB < m) {
  if (arrA[indexA] <= arrB[indexB]) {
    result += arrA[indexA] + " ";
    indexA++;
  } else {
    result += arrB[indexB] + " ";
    indexB++;
  }
}

console.log(result);
