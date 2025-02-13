let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let s = input[0];

let check = [0, 0];
check[s[0]] = 1;
for (let i = 1; i < s.length; i++) {
  if (s[i] == s[i - 1]) continue;
  else {
    check[s[i]] += 1;
  }
}

console.log(Math.min(...check));
