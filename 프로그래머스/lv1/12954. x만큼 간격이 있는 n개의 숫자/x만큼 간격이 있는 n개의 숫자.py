def solution(x, n):
    answer = []
    if x == 0:
        answer = [0] * n
    else:
        i = x
        while i != x*(n+1):
            answer.append(i)
            i += x
    
    
    return answer