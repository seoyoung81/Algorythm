def solution(n):
    answer = 0
    memo = [0, 1, 1] + [0] * n
    for i in range(3, n+2):
        memo[i] = memo[i-1] + memo[i-2]
    answer = memo[n] % 1234567
    return answer