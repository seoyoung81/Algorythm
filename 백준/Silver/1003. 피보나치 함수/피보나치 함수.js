let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let d = new Array(45).fill(0);
d[1] = d[2] = 1;
for (let i = 3; i < 45; i++) {
  d[i] = d[i - 1] + d[i - 2];
}

let testCase = Number(input[0]);
for (let ts = 0; ts < testCase; ts++) {
  let result = "";
  let n = Number(input[ts + 1]);
  if (n == 0) {
    result += "1 0";
  } else {
    result += d[n - 1] + " ";
    result += d[n];
  }

  console.log(result);
}
