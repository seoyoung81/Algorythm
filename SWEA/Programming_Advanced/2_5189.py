def dfs(cur, start, total):
    global result

    # 종료 조건
    if cur == N - 1:  # 모든 사무실을 다 돌면 종료
        result = min(result, arr[start][0] + total)     # 마지막엔 무조건 사무실로 간다
        return

    # 하부 호출
    for i in range(1, N):
        if visited[i] == 0 and start != i:      # 그 행에 방문하지 않았다면, 대각선이 아닌 경우
            visited[i] = 1  # 방문하기
            dfs(cur+1, i, total + arr[start][i])
            visited[i] = 0  # 다시 0으로 ??

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # N x N arr
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1001
    visited = [0 for _ in range(N)]
    dfs(0, 0, 0)
    print(f'#{test_case}', result)
