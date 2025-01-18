let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [A, B] = input[0].split(" ").map(Number);
let result = 0;

while (A != B) {
  if (A > B) {
    result = -2;
    break;
  }
  if (B % 2 == 0) B /= 2;
  else {
    let str_B = String(B);
    if (str_B[str_B.length - 1] == "1")
      B = Number(str_B.slice(0, str_B.length - 1));
    else {
      result = -2;
      break;
    }
  }
  result += 1;
}

console.log(result + 1);
