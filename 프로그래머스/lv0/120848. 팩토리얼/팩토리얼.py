def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    else:
        return 1

def solution(n):
    answer = 0
    
    for i in range(10, 0, -1):
        if n == factorial(i):
            answer = i
        elif n < factorial(i):
            answer = i-1
    return answer