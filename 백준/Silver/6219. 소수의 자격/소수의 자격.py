A, B, D = map(int, input().split())
prime = [1] * (B+1)

# 에라토스테네스의 체 소수 구하
for i in range(2, int(B**0.5)+1):
    if prime[i]:
        for j in range(i+i, B+1, i):
            prime[j] = 0

number = [i for i in range(A, B+1) if prime[i]]

cnt = 0
for n in number:
    if str(D) in str(n):
        cnt += 1
print(cnt)