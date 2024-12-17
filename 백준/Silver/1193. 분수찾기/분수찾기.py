x = int(input())

arr = [1] + [0] * (x//2+1)
for i in range(1, x//2+1):
  arr[i] = arr[i-1] + i+1

group = 0
for i in range(x):
  if arr[i] >= x:
    group = i + 1
    break


number = x - arr[group-2]

# 분수
a = 0
b = 0

# group이 홀수라면
if group % 2:
  b = number
  a = group - b + 1
else:
  a = number
  b = group - a + 1 

print(f"{a}/{b}")