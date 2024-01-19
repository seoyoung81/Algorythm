import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

s = 0
e = n-1
result = 2000000000
a, b = 0, 0

while s < e:
    sub = numbers[s] + numbers[e]

    # 차이 계산해서 result 업데이트
    if abs(sub) <= result:
        a = numbers[s]
        b = numbers[e]
        result = abs(sub)
    
    if sub <= 0:
        s += 1
    
    else:
        e -= 1

print(a, b)