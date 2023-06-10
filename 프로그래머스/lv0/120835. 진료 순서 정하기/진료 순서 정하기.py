def solution(emergency):
    answer = []
    # 얕은 복사
    lst = emergency[:]
    lst.sort(reverse=True)
    print(lst)
    
    for num in emergency:
        for j in range(len(lst)):
            if num == lst[j]:
                answer.append(j+1)
                
           
    
    return answer