def dfs(i, j):
    q = [i, j]
    visited[i][j] = 1
    while q:
        u = q.pop(0)
        v = q.pop(0)
        # print((u, v), end=' ')
        if visited[v][i] == 0:
            visited[v][i] = visited[v][w] + 1
            dfs(i)

N, M = map(int, input().split())    # 연구소의 크기 NxN arr / 놓을 수 있는 바이러스 개수
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*(N+1) for _ in range(N+1)]
