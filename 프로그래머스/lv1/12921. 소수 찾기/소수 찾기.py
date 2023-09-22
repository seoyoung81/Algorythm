def checkDecimal(n):
    m = int(n**0.5)
    for i in range(2, m+1):
        if n % i == 0:
            return 0
    return 1

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if checkDecimal(i):
            answer +=1
    
    return answer