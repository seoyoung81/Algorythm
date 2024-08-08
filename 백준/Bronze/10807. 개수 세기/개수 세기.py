N = int(input())
numbers = list(map(int, input().split()))
v = int(input())
result = 0

for num in numbers:
  if num == v:
    result += 1

print(result)