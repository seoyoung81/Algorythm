let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let data = input.slice(1, N+1);

// 중복 제거
data = [...new Set(data)];

function compare(a, b) {
  if (a.length != b.length) return a.length - b.length;
  else {
    if (a < b) return -1;
    else if (a > b) return 1;
    else return 0;
  }
}

data.sort(compare);

let result = "";
for (let char of data) {
  result += char + "\n";
}
console.log(result);
