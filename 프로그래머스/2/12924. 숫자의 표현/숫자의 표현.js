function solution(n) {
  let answer = 0;
  let now = 1, cnt = 1, plus = 0;

  while(cnt <= n) {
    plus = plus + now;
    if(plus >= n) {
      if(plus === n) answer++;
      plus = 0;
      cnt++;
      now = cnt;
    } else {
      now++;
    }
  }

  return answer;
}