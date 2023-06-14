def solution(n):
    cnt = 0
    answer = 0
    for i in range(1, 200):
        if not ('3' in str(i) or i%3==0):
            cnt += 1
        if cnt == n:
            answer = i
            break
            
    return answer