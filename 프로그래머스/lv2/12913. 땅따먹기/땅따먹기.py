def solution(land):
    answer = 0
    m = len(land)
    n = len(land[0])
    for i in range(1,m):
        for j in range(n):
            # 가장 max 값을 계속 누적시켜서 최적의 경로를 찾자
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    
    answer = max(land[m-1])
    return answer