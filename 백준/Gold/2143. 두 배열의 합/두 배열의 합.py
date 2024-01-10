import bisect
T = int(input()) # 합
n = int(input())    # A 의 개수
A_lst = list(map(int, input().split()))
m = int(input())    # B 의 개수
B_lst = list(map(int, input().split()))

A_sum = []
B_sum = []
for i in range(n):
    s = A_lst[i]
    A_sum.append(s)
    for j in range(i+1, n):
        s += A_lst[j]
        A_sum.append(s)
for i in range(m):
    s = B_lst[i]
    B_sum.append(s)
    for j in range(i+1, m):
        s += B_lst[j]
        B_sum.append(s)

A_sum.sort()
B_sum.sort()

### 이분 탐색
result = 0
for i in range(len(A_sum)):
    a = bisect.bisect_left(B_sum,T-A_sum[i])
    b = bisect.bisect_right(B_sum,T-A_sum[i])
    result += b - a
print(result)
