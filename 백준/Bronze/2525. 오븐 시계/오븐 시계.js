let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

time = input[0].split(" ").map(Number);
H = time[0];
M = time[1];

cooking = Number(input[1]);

M = M + cooking;

if (M >= 60) {
  H += parseInt(M / 60);
  M -= 60 * parseInt(M / 60);
}

if (H >= 24) {
  H -= 24;
}

console.log(H, M);
