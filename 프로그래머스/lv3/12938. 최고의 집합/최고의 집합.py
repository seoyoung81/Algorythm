def solution(n, s):
    answer = []
    ## 2개인 경우만 해보자
    if n >= s:
        answer = [-1]
    # else:
    #     if s % 2:
    #         answer = [s//2, s//2+1]
    #     else:
    #         answer = [s//2, s//2]
    
    ### 3개인 경우
    # 8인데 3이라면 3,3,2
    
    else: 
        q = s // n
        r = s % n
        answer = [q] * n
        for i in range(r):
            answer[i] += 1
    
    answer.sort()
    '''
    3, 3, 3, 3, 2, 2, 2, 2 81*16 1296
    6, 2, 2, 2, 2, 2, 2, 2 6*128 768
    '''
    
    return answer