N, K = map(int, input().split())
coin = []
for _ in range(N):
  coin.append(int(input()))

sum = 0

for i in range(N-1, -1, -1):
  if K == 0:
    break
  sum += K // coin[i]
  K = K % coin[i]

print(sum)