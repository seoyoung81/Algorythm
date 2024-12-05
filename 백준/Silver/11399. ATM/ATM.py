N = int(input())
time = sorted(list(map(int, input().split())), reverse=True)
sum = 0

for i in range(N):
  sum += time[i] * (i+1)

print(sum)