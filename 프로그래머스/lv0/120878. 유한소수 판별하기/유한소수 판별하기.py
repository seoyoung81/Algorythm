def solution(a, b):
    answer = 2
   
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    print(b)
    if b == 1:
        answer = 1
    else:
        if a % b == 0:
            answer = 1
   

    return answer