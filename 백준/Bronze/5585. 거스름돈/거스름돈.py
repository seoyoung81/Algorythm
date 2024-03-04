n = int(input())

a = 1000 - n
money = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in range(6):
  if a <= 0:
    break
  cnt += a // money[i]
  a -= (a // money[i]) * money[i]
  
print(cnt)
