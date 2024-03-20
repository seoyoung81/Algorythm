def solution(elements):
    result = set()
    n = len(elements)
    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    elements = elements * 2
    
    for i in range(n):
        for j in range(n):
            result.add(sum(elements[j:j+i+1]))
    return len(result)