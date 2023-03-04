def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, V+1):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)

T = 1
for test_case in range(1, T + 1):
    V, E = map(int, input().split())    # 정점 개수, 간선 개수
    visited = [0] * (V+1)
    arr = [[0] * (V+1) for _ in range(V+1)]
    numbers = list(map(int, input().split()))

    for i in range(E):
        n1, n2 = numbers[i*2], numbers[i*2+1]
        arr[n1][n2] = 1

    dfs(8)
