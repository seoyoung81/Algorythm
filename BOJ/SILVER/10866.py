from collections import deque
from sys import stdin

N = int(stdin.readline())
deq = deque()
for _ in range(N):
    s = list(map(str, stdin.readline().split()))
    if s[0] == 'push_front':
        deq.appendleft(int(s[1]))
    elif s[0] == 'push_back':
        deq.append(int(s[1]))
    elif s[0] == 'pop_front':
        if deq:
            a = deq.popleft()
            print(a)
        else:
            print(-1)
    elif s[0] == 'pop_back':
        if deq:
            a = deq.pop()
            print(a)
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(deq))
    elif s[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)