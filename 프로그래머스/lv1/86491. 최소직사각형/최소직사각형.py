def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    size1 = sorted(sizes)
    a = size1[-1][0]
    sizes.sort(key=lambda x: x[1])
    b = sizes[-1][1]
    answer = a * b
    return answer