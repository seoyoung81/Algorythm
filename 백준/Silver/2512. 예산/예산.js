let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let budget_arr = input[1].split(" ").map(Number);
let budget = Number(input[2]);

// 예산을 오름차순으로 정렬
budget_arr.sort((a, b) => a - b);

// 초기 설정
let remaining_budget = budget;
let result = 0;

for (let i = 0; i < N; i++) {
  let avg = Math.floor(remaining_budget / (N - i)); // 남은 예산의 평균
  if (budget_arr[i] <= avg) {
    // 요청한 예산이 평균보다 작거나 같은 경우
    remaining_budget -= budget_arr[i];
    result = budget_arr[i];
  } else {
    // 요청 예산이 평균보다 큰 경우, 상한액은 평균으로 고정
    result = avg;
    break;
  }
}

// 평균보다 작을 때
if (result === 0) {
  result = Math.min(...budget_arr); 
}

console.log(result);
