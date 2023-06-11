def solution(s):
    answer = []
    stack = []
    duplication = []
    for str in s:
        if not str in stack:
            stack.append(str)
        else:
            duplication.append(str)
            
    for alpha in stack:
        if alpha not in duplication:
            answer.append(alpha)
    
    answer.sort()
             
    return ''.join(answer)