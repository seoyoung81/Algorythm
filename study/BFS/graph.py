'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs1(v, k):     # 중복없이 빠짐없이
    visited[v] = 1  # 중복 방지용
    print(v)
    # for w in adjL[v]:   # v와 인접하고
    #     if visited[w] == 0:
    #         dfs1(w, k)
    for w in range(1, k+1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs1(w, k)

def dfs2(s, k):
    stack = []
    visited = [0] * (k+1)
    v = s
    while True:
        if visited[v] == 0:
            print(v)
            visited[v] = 1
        for w in range(1, k+1):
            if adjM[v][w] and visited[w] == 0:
                stack.append(v)
                v = w
        else:   # 더이상 인접인 정점이 없으면
            if stack:
                v = stack.pop()
            else:
                break
    return

def dfs3(v, k, g):
    global cnt
    if v==g:
        cnt += 1    # 목적지 도착 횟수
    else:
        visited[v] = 1  # 중복 방지용

        for w in range(1, k + 1):
            if adjM[v][w] == 1 and visited[w] == 0:
                dfs3(w, k, g)
        visited[v] = 0




V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1
    adjL[n1].append(n2)
    adjL[n2].append(n1)

visited = [0] * (V+1)
cnt = 0
dfs1(1, V)
dfs2(1, V)
dfs3(1, V, 7)


