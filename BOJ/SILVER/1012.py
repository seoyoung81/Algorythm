import sys
sys.setrecursionlimit(10**5)
T = int(input())
for test_case in range(1, T + 1):
    M, N, K = map(int, input().split())    # 가로/세로, 배추 개수
    arr = [[0]*(M+1) for _ in range(N+1)]   # 배추 위치 담기
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    def dfs(i, j):
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1:    # 주변에 배추가 있다면
                    arr[ni][nj] = -1    # -1 로 만들고
                    dfs(ni, nj)     # 다시 탐색



    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)
