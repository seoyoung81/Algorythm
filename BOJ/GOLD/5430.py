import sys
from collections import deque

# test case
T = int(input())
for test_case in range(T):
    p = input() #수행할 함수 p
    n = int(input()) #배열에 들어있는 수의 개수
    # , 를 기준으로 나누
    arr = input().rstrip()[1:-1].split(",") #배열에 들어 있는 정수자
    # print(arr) -> 문자열
    queue = deque(arr)

    # 뒤집기 한 번만 실행하기 위해서 !
    flag = 0

    # n 이 0이면 queue 초기
    if n == 0:
        queue = []


    for str in p:
        if str == 'R':
            flag += 1
        elif str == 'D':
            if len(queue) == 0:
                print('error')
                break
            else:
                # 홀수면 뒤에서 삭제하고 (뒤집을거여서)
                if flag % 2:
                    queue.pop()
                else:
                    queue.popleft()

    # n이 0이 아니면
    else:
        # flag 가 홀수면 한 번 뒤집기
        if flag % 2:
            queue.reverse()
        print('[' + ','.join(queue) + ']')
