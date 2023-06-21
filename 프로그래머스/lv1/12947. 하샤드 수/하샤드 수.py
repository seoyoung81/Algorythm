def solution(x):
    answer = True
    sumV = 0
    
    for num in str(x):
        sumV += int(num)
    
    if x % sumV == 0:
        answer = True
    else:
        answer = False
        
    
    return answer