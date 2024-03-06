t = int(input())
for _ in range(t):
  animals = list(map(str, input().split()))
  notFox = []
  for i in range(100):
    lst = list(map(str, input().split()))
    if lst[0] == 'what':
      break
    notFox.append(lst[2])
  
  result = []
  for char in animals:
    if char not in notFox:
      result.append(char)
  print(*result)