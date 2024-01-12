import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = [0] + list(map(int, input().split()))
number_sum = [0] * (N+1)

for i in range(1, N+1):
    number_sum[i] = number_sum[i-1] + number[i]

result = min(number) * K
for i in range(K, N+1):
    if result < number_sum[i] - number_sum[i-K]:
        result = number_sum[i] - number_sum[i-K]

print(result)
