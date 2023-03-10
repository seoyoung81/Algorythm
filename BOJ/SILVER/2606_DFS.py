N = int(input())    # 컴퓨터의 개수
M = int(input())    # 연결되어 있는 컴퓨터 쌍의 수
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
computer = []
for _ in range(M):  # 노드 정보 입력
    n1, n2 = map(int, input().split())  # 양방향으로 연결
    arr[n1][n2] = 1
    arr[n2][n1] = 1

def dfs(v):
    visited[v] = 1  # 방문한 좌표 찍기
    computer.append(v)
    for w in range(1, N+1):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)

dfs(1)
print(len(computer)-1)

