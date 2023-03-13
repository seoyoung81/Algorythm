N = int(input())    # 트리의 정점 개수
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())    # 간선 정보
    tree[a].append(b)
    tree[b].append(a)