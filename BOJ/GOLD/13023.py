N, M = map(int, input().split())    # 사람의 수, 친구 관계의 수
arr = [[] for _ in range(N)]
visited = [0] * N
result = 0

for _ in range(M):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)
# print(arr) [[1], [0, 2], [1, 3], [2, 4], [3]]

def dfs(v,d):   # v 는 시작점, d 는 깊이
    global result
    visited[v] = 1  # 방문 찍기
    # print(visited)
    # print(v, w)
    if d == 5:  # 깊이가 5가 되면 친구 관계 완성
        result = 1
        return
    for i in arr[v]:
        if visited[i] == 0:     # 방문하지 않은 곳이라면
            dfs(i, d+1)         # 깊이 1 더하고 재귀 돌리기
    visited[v] = 0

# 전체 탐색
for i in range(N):
    dfs(i, 1)
    if result == 1:
        break

if result == 1:
    print(1)
else:
    print(0)

