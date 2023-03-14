def dfs(i, j):
    if arr[i][j] == '-':
        arr[i][j] = 1   # 방문처리
        for dj in [1, -1]:  # 좌우 확인
            nj = j + dj
            if 0 < nj < M and arr[i][nj] == '-':  # 범위를 벗어나지 않고 -모양이면
                dfs(i, nj)
    elif arr[i][j] == '|':
        arr[i][j] = 1   # 방문처리
        for di in [1, -1]:  # 상하 확인
            ni = i + di
            if 0 < ni < N and arr[ni][j] == '|':
                dfs(ni, j)

N, M = map(int, input().split())    # 세로 / 가로
arr = []
for _ in range(N):
    arr.append(list(input()))

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '-' or arr[i][j] == '|':
            dfs(i, j)
            cnt += 1
print(cnt)

