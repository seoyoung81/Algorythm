n, m = map(int, input().split())    # 수의 개수, 수의 합 m
numbers = list(map(int, input().split()))

l = 0
r = 1
result = 0
while r <= n and l <= r:
    if sum(numbers[l:r]) == m:
        result += 1
        r += 1
    elif sum(numbers[l:r]) < m:
        r += 1
    else:
        l += 1

print(result)

