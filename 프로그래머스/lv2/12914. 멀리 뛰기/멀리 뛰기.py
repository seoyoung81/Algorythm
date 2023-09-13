def solution(n):
    answer = 0
    memo = [0] * 2001
    memo[0] = 1
    memo[1] = 2
    for i in range(2, 2000):
        memo[i] = memo[i-1] + memo[i-2]
        
    answer = memo[n-1]
    answer %= 1234567
    return answer

