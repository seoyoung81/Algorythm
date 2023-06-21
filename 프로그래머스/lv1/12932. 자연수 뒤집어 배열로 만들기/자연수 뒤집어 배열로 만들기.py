def solution(n):
    answer = []
    lst = list(str(n))
    for num in lst:
        answer.append(int(num))
    
    answer = answer[::-1]
    return answer