import sys
sys.setrecursionlimit(10**5)

N = int(input())    # 트리의 정점 개수
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)
distance = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())    # 간선 정보
    tree[a].append(b)
    tree[b].append(a)

# print(tree) [[], [2], [1, 3, 4], [2], [2]]
def dfs(n):
    visited[n] = 1
    for i in tree[n]:
        if visited[i] == 0:
            distance[i] = distance[n] + 1
            dfs(i)

dfs(1)
# print(distance) [0, 0, 1, 2, 2]
answer = 0
for i in range(2, N+1):
    if len(tree[i]) == 1:
        answer += distance[i]
        # print(answer)


# 성원이가 이기려면 answer 값이 홀수여야 한다
if answer % 2 == 0:
    print('No')
else:
    print('YES')