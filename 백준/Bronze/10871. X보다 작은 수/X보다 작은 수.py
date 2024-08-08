N, X = map(int, input().split())
numbers = list(map(int, input().split()))
result = []

for num in numbers:
  if num < X:
    result.append(num)

print(*result)