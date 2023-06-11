T = int(input())    # test case
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())     # 붕어빵 먹을 수 있는 N명, M초의 시간동안, K개 붕어빵 만들 수 있음 (2초 동안 2개)
    people = sorted(list(map(int, input().split())))      # 붕어빵 먹을 수 있는 N명이 언제 도착하는지 초 단위 ( 3초, 4초)

    boong_lst = [0] * 11112
    for i in range(1, 11112):
        if i % M == 0:  # M의 배수인 곳에
            boong_lst[i] += K   # 붕어빵 K개 추가

    # print(boong_lst)
    result = ''
    for i in people:    # 모든 사람들에 대해서
        if sum(boong_lst[:i+1]) <= 0:   # 내 앞에 붕어빵의 개수의 합이 0보다 작거나 같으면
            result = 'Impossible'       # 붕어빵 못 먹음!
        else:
            boong_lst[i] -= 1           # 아니라면 한 개 먹음


    if result == '':
        result = 'Possible'

    print(f'#{test_case}', result)