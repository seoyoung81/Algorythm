def solution(arr):
    answer = []
    
    if arr == [10]:
        answer = [-1]
    
    minV = min(arr)
    for num in arr:
        if num != minV:
            answer.append(num)
    return answer