N = int(input())
lst = []
r = N // 3

for i in range(r, -1, -1):
    a = N - i * 3
    b = a % 5
    if b == 0:
      lst.append(i + a//5)

if lst:
  print(min(lst))
else:
  print(-1)
