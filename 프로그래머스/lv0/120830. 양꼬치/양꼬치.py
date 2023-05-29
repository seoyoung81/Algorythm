def solution(n, k):
    answer = 12000 * n + 2000 * k
    yang = n // 10
    answer -= yang * 2000
    
    return answer