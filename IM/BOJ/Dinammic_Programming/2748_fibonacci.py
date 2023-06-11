# def fibo(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# n = int(input())
# print(fibo(n))

# memoization
n = int(input())
memo = [0] * (n+1)
memo[1] = 1

for i in range(2, n+1):
    memo[i] = memo[i-1] + memo[i-2]


print(memo[n])

# 반복문
