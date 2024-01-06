C = int(input())
# 최대공약수가 1인 것 찾
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

result = [0 for _ in range(1001)]
result[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i == j:
            continue

        if gcd(i, j) == 1:
            cnt += 2
    result[i] = result[i-1] + cnt

for _ in range(C):
    N = int(input())
    print(result[N])


