def solution(my_str, n):
    answer = []
    m = len(my_str)
    for i in range(m//n):
        answer.append(my_str[i*n:(i+1)*n])
    
    if m % n:
        answer.append(my_str[m-(m%n):])
    return answer