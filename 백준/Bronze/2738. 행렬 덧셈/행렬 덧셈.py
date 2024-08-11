N, M = map(int, input().split())
A = []
B = []
C = [[] for _ in range(N)]

for _ in range(N):
    arr = list(map(int, input().split()))
    A.append(arr)

for i in range(N):
    arr = list(map(int, input().split()))
    B.append(arr)

for i in range(N):
    for j in range(M):
        C[i].append(A[i][j] + B[i][j])

for i in range(N):
  print(*C[i])

