function solution(n) {
    var answer = 0;
    let memo = new Array(n+1);
    
    memo[0] = 0;
    memo[1] = 1;
    memo[2] = 1;

    for (let i=3; i<n+2; i++) {
        memo[i] = (memo[i-1] + memo[i-2]) % 1234567
    } 
    answer = memo[n]
    return answer;
}
