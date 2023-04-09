from sys import stdin
from collections import deque


# N : 큐에 처음 포함되어 있던 수
# M : 뽑아내려고 하는 원소의 개수
N, M = map(int, stdin.readline().split())
idx = list(map(int, stdin.readline().split())) # 뽑아내려고 하는 수의 위치
numbers = deque(i for i in range(1, N+1))

cnt = 0
for i in idx:
    while True:
        if numbers[0] == i:
            numbers.popleft()
            break
        else:
            if numbers.index(i) < len(numbers)/2:
                while numbers[0] != i:
                    numbers.append(numbers.popleft())
                    cnt += 1
            else:
                while numbers[0] != i:
                    numbers.appendleft(numbers.pop())
                    cnt += 1


print(cnt)




