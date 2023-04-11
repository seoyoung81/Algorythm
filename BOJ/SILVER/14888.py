N = int(input())    # 수의 개수
numbers = list(map(int, input().split()))   # A 의 개수
add, sub, mul, div = map(int, input().split())   # 연산기호의 개수
# 덧셈, 뺄셈, 곱셈, 나눗셈

max_value = -1e9
min_value = 1e9

def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value

    if i == N:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr / numbers[i]))
            div += 1

dfs(1, numbers[0])

print(max_value)
print(min_value)
