let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

let M = Math.max(...arr);

let summary = arr.reduce((a, b) => a + b);
let avg = summary / n;


console.log(avg / M * 100);
