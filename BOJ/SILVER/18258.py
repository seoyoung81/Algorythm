from sys import stdin
from collections import deque

N = int(stdin.readline())
q = deque()
for _ in range(N):
    s = list(map(str, stdin.readline().split()))
    if s[0] == 'push':
        q.append(int(s[1]))     # q에 정수 넣기
    elif s[0] == 'pop':
        if q:               # q가 비어있지 않은 경우
            a = q.popleft()    # 가장 앞에 있는 정수 빼기
            print(a)
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q:   # q가 비어있으면
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)


