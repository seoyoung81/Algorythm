def solution(array):
    answer = 0
    m = max(array)
    cnt_lst = [0] * (m+1)
    for num in array:
        cnt_lst[num] += 1
    
    maxV = max(cnt_lst)
    if cnt_lst.count(maxV) >= 2:
        answer = -1
    else:
        answer = cnt_lst.index(maxV)
        
        
    return answer