from collections import deque
N, K = map(int, input().split())

q = deque([i for i in range(1, N+1)])
result = []

while len(q) != 0:
    for _ in range(K-1):
        q.append(q.popleft())

    a = q.popleft()
    result.append(a)



print(f'<', end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print(f'>', end='')