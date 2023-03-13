import sys
sys.setrecursionlimit(10**6)

N = int(input())    # 노드의 개수
tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)
# 노드 정보 담
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

# print(tree) [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

def dfs(n):
    for i in tree[n]:
        if parent[i] == 0:  # 노드 정보가 없다면
            parent[i] = n   # 노드 기록하기
            # print(parent)   [0, 6, 4, 6, 1, 3, 1, 4]
            dfs(i)

# 트리의 루트는 1
dfs(1)

for i in range(2, N+1):
    print(parent[i])



