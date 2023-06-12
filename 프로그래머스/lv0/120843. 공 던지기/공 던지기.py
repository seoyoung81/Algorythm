def solution(numbers, k):
    answer = 0
    m = len(numbers)
    k = 2*k
    if k > m:
        k = k % m
    
    answer = numbers[k-2]
    return answer