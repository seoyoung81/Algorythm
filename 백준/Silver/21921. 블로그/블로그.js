let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, x] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number);

let end = x;
let cnt = [];

let xSum = 0;
for (let i = 0; i < end; i++) {
  xSum += arr[i];
}
cnt.push(xSum);

for (let start = 0; start < n - x; start++) {
  xSum -= arr[start];
  xSum += arr[end];
  end++;
  cnt.push(xSum);
}

let maxSum = Math.max(...cnt);
let result = 0;
if (maxSum == 0) console.log("SAD");
else {
  cnt.sort((a, b) => b - a);

  for (let i = 0; i < cnt.length; i++) {
    if (cnt[i] == maxSum) result++;
    else break;
  }
  console.log(maxSum);
  console.log(result);
}
