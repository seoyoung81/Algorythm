let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
for (let i = 0; i < n; i++) {
  data = input[i + 1].split(" ").map(Number);
  student = data[0];
  average = (data.reduce((a, b) => a + b) - student) / student;
  let percent = 0;
  // 비율 구하기
  for (let j = 1; j <= student; j++) {
    if (data[j] > average) percent += 1;
  }

  console.log(`${((percent / student) * 100).toFixed(3)}%`);
}
