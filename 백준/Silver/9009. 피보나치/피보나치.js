let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

// 피보나치 수열
let fibo = new Array(100).fill(0);
fibo[0] = 0;
fibo[1] = 1;
for (let i = 2; i < 101; i++) {
  fibo[i] = fibo[i - 1] + fibo[i - 2];
}

let T = Number(input[0]);
for (let i = 1; i < T + 1; i++) {
  let num = Number(input[i]);
  let result = [];
  for (let j = 100; j >= 0; j--) {
    if (num >= fibo[j]) {
      num -= fibo[j];
      result.push(fibo[j]);
    }

    if (num == 0) break;
  }

  // print
  let answer = "";
  for (let k = result.length - 1; k >= 0; k--) {
    answer += result[k] + " ";
  }
  console.log(answer);
}
