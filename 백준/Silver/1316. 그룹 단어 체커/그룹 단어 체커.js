let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let result = 0;

for (let i = 1; i < n + 1; i++) {
  let word = input[i];
  let mySet = new Set();
  let isGroupWord = true;
  for (let j = 0; j < word.length; j++) {
    if (word[j] != word[j + 1]) {
      if (mySet.has(word[j])) {
        isGroupWord = false;
        break;
      } else {
        mySet.add(word[j]);
      }
    }
  }

  if (isGroupWord) {
    result += 1;
  }
}

console.log(result);
