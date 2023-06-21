def solution(n):
    answer = 0
    i = 1
    while True:
        if n == i * i:
            answer = (i + 1) ** 2
            break
        
        if n < i * i:
            answer = -1
            break
            
        i += 1
    
    return answer