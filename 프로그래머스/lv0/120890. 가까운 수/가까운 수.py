def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    print(array)
    
    idx = array.index(n)
    a = abs(array[idx-1] - n)
    if idx == (len(array)-1):
        answer = array[idx-1]
    else:
        b = abs(array[idx+1] - n)
    
        if a > b:
            answer = array[idx+1]
        elif a <= b:
            answer = array[idx-1]
    
    return answer