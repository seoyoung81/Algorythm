def dfs(n, sm):
    global result
    # 가지 치기
    if n < N and sm > result:
        return

    # 종료 조건
    if n == N:
        result = min(result, sm)
        return

    # 하부 호출
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, sm + arr[n][i])
            visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 1600
    dfs(0, 0)
    print(f'#{test_case}', result)