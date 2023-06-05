def solution(array):
    maxV = max(array)
    answer = [maxV]
    for i in range(len(array)):
        if array[i] == maxV:
            answer.append(i)
    
    return answer