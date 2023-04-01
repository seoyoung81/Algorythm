def dfs(cnt, idx):
    global result
    # 종료 조건
    if cnt == N//2:     # 팀에 절반이 들어오면 종료
        teamA = teamB = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    teamA += arr[i][j]
                elif not visited[i] and not visited[j]:
                    teamB += arr[i][j]
        result = min(result, abs(teamA-teamB))
        return

    # 하부 호출
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, i+1)
            visited[i] = 0



N = int(input())    # even
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
result = 1000000000
dfs(0, 0)
print(result)