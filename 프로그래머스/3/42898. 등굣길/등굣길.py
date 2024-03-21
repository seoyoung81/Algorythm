def solution(m, n, puddles):
    answer = 0
    map = [[0] * (m + 1) for i in range(n + 1)] 
    map[1][1] = 1
    puddles = [[q,p] for [p,q] in puddles]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            elif [i, j] in puddles:
                map[i][j] = 0
            else:
                map[i][j] = map[i-1][j] + map[i][j-1]

    return map[-1][-1] % 1000000007