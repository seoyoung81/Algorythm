import sys
input = sys.stdin.readline

g = int(input())  
# 성원이의 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것

weight = [i*i for i in range(100001)]

a = 1
b = 2
result = []

while a<=100001 and b<=100001 and a<b:
    if weight[b] - weight[a] == g:
        result.append(b)
        a += 1
        b += 1
    elif weight[b] - weight[a] > g:
        a += 1
    else:
        b += 1

if result:
    for num in result:
        print(num)
else:
    print(-1)
