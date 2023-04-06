n = int(input())
stack = []
answer = []
flag = 0
cur = 1

for i in range(n):
    num = int(input())
    while cur <= num:   # num 이랑 같아질 때까지 push
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == num:    # 마지막 값이 num이랑 같으면
        stack.pop()         # pop
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)