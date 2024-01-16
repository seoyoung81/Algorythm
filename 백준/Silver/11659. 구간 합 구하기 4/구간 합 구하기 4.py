import sys
input = sys.stdin.readline

N, M = map(int, input().split())

number = list(map(int, input().split()))
sum = [0] * (N+1)
for i in range(1, N+1):
    sum[i] = sum[i-1] + number[i-1]

for _ in range(M):
    a, b = map(int, input().split())
    print(sum[b]-sum[a-1])
