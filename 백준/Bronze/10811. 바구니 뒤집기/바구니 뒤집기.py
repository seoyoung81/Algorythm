N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    numbers[i-1:j] = list(reversed(numbers[i-1:j]))

print(*numbers)