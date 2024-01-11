import sys
input = sys.stdin.readline
N, M = map(int, input().split())

number = []
for _ in range(N):
    lst = list(map(int, input().split()))
    number.append(lst)

number_sum = [[0]*(N+1) for _ in range(N+1)]
# (x, y) 까지의 누적합 구해놓기
for i in range(1, N+1):
    for j in range(1, N+1):
        number_sum[i][j] = number_sum[i-1][j] + number_sum[i][j-1] - number_sum[i-1][j-1] + number[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(number_sum[x2][y2]-number_sum[x2][y1-1]-number_sum[x1-1][y2]+number_sum[x1-1][y1-1])
