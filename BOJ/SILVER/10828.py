import sys

N = int(input())
stack = []
for _ in range(N):
    lst = list(map(str, sys.stdin.readline().split()))
    a = lst[0]
    if len(lst) == 2:
        num = int(lst[-1])

    if a == 'push':
        stack.append(num)

    elif a == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            c = stack.pop()
            print(c)

    elif a == 'size':
        print(len(stack))

    elif a == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif a == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])