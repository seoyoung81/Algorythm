N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    a = numbers[i-1]
    b = numbers[j-1]
    numbers[i-1] = b
    numbers[j-1] = a

print(*numbers)
