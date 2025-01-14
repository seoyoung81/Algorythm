let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split("\n");

n = Number(input[0])
result = ''
for(let i=1; i<=n; i++) {
  let [a, b] = input[i].split(' ').map(Number)
  result += String(a+b)
  result += '\n'
}

console.log(result)