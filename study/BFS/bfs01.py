V, E =




def dfs(v): # 지금 현재 탐색하는 정점 v
    visited[v] = 1  # 방문기록 찍기 -> 다시 안 오려고
    print(v, end=' ')   # 방문한 곳 출력
    # v에 인접한 정점 중에 방문하지 않은 곳 방문하기
    for w in range(1, V+1):
        if arr[v][w] == 1 and visited[w] == 0:  # 길이 있고, 방문한 적이 없다면
            dfs(w)  # w 도 dfs 돌기

dfs(1)  # 1부터 시작

