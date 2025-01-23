let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]); // 카드의 개수
let cards = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b); // 카드 숫자
let M = Number(input[2]);
let arr = input[3].split(" ").map(Number); // 몇 개 가지고 있나?

// loweBound
function lowerBound(arr, x, start, end) {
  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (arr[mid] >= x) end = mid;
    else start = mid + 1;
  }
  return end;
}

// upperBound
function upperBound(arr, x, start, end) {
  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (arr[mid] > x) end = mid;
    else start = mid + 1;
  }
  return end;
}

function countNum(arr, value) {
  let right = upperBound(arr, value, 0, arr.length);
  let left = lowerBound(arr, value, 0, arr.length);
  return right - left;
}

let result = "";
for (num of arr) {
  let countValue = countNum(cards, num);
  result += countValue + " ";
}

console.log(result);
