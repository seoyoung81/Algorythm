t = int(input())
for _ in range(t):
  j, n = map(int, input().split())
  candy = []
  for _ in range(n):
    a, b = map(int, input().split())
    candy.append(a*b)
  
  candy = sorted(candy, reverse=True)

  i = 0
  while j > 0:
    j -= candy[i]
    i += 1
  
  print(i)