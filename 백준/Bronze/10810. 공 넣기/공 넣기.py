N, M = map(int, input().split())
numbers = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    numbers[i:j+1] = [k] * (j-i+1)

print(*numbers[1:])
