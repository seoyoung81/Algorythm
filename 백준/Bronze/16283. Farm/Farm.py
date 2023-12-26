a, b, n, w = map(int, input().split())
# 양 사료, 염소 사료, 전체 몇마리, 전체 사료
result = 0
sheep = 0
goat = 0
for i in range(1, n):
    if a*i + b*(n-i) == w:
        result += 1
        sheep = i
        goat = n-i

if result == 1:
    print(sheep, goat)
else:
    print(-1)