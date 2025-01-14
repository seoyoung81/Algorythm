let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split("\n");

data = input[0].split(" ").map(Number);
H = data[0];
M = data[1];

if (M < 45) {
  if (H === 0) {
    H = 23;
  } else {
    H -= 1;
  }
  M = M + 15;
} else {
  M = M - 45;
}

console.log(H, M)
