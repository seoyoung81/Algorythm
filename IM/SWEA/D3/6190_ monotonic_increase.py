T = int(input())
<<<<<<< HEAD
for test_case in range(1, T+ 1):
    N = int(input())    # N개의 정수
    numbers = list(map(int, input().split()))
=======
for test_case in range(1, T + 1):
    N = int(input())    # N개의 수가 주어진다
    numbers = list(map(int, input().split()))

    monotonic = []
    not_monotonic = []

    for i in range(N):
        for j in range(i+1, N):
            a = str(numbers[i] * numbers[j])
            monotonic.append(int(a))
            for i in range(len(a)-1):
                if a[i] > a[i+1]:   # 단조 증가가 아니라면
                 not_monotonic.append(int(a))

    print(monotonic)
    print(not_monotonic)

    for num in not_monotonic:
        if num not in monotonic:



    # print(monotonic_list)
    # max_list = []
    # m = len(monotonic_list)
    # for i in range(m):
    #     for j in range(m-1):
    #         if int(monotonic_list[i][j]) <= int(monotonic_list[i][j+1]):   # 단조 증가이면
    #             max_list.append(int(monotonic_list[i]))

    # print(max_list)
    # print(f'#{test_case}',max(max_list))

    '''
    
1
4
2 4 7 10
    '''
>>>>>>> a9db90fe2bf81e409aceda66a828c4cf109f47a8
