def solution(n, m):
    answer = []
    p = max(n, m)
    q = min(n, m)
    for i in range(p, 0, -1):
        if p % i == 0 and q % i == 0:
            answer.append(i)
            break
    answer.append(n*m//answer[0])
    return answer