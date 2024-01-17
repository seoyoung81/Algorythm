n = int(input()) # 수열의 크기
numbers = list(map(int, input().split()))   # 수열에 포함되는 수
x = int(input())    # 두 수의 합

numbers.sort()
result = 0
s = 0
e = n-1
while s < e:
    if numbers[s] + numbers[e] == x:
        result += 1
        s += 1
        e -= 1
    elif numbers[s] + numbers[e] < x:
        s += 1
    else:
        e -= 1

print(result)