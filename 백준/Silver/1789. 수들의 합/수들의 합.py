S = int(input())

sum = 0
result = 0
for i in range(1, S+1):
  sum += i
  result = i
  if sum > S:
    break

if S == 1:
  print(1)
else:
  print(result-1)
