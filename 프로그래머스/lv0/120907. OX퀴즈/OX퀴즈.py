def solution(quiz):
    answer = []
    for lst in quiz:
        exp = list(lst.split(' '))
        if exp[1] == '+':
            if int(exp[0]) + int(exp[2]) == int(exp[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(exp[0]) - int(exp[2]) == int(exp[4]):
                answer.append('O')
            else:
                answer.append('X')
                
    return answer