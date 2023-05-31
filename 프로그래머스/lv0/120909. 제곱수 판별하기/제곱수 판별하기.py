def solution(n):
    answer = 2
    for i in range(1, 1001):
        if i * i == n:
            answer = 1
            break
    return answer