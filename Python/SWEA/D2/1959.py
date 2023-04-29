T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N, M 개의 숫자들로 이루어진 문자열
    A_numbers = list(map(int, input().split()))
    B_numbers = list(map(int, input().split()))

    # 전체 합을 담을 리스트
    total_lst = []
    if N <= M:
        for k in range(M - N + 1):
            total = 0
            for i in range(N):
                total += (A_numbers[i] * B_numbers[i+k])
            total_lst.append(total)

    else:
        for k in range(N - M + 1):
            total = 0
            for i in range(M):
                total += (A_numbers[i+k] * B_numbers[i])
            total_lst.append(total)

    # print(total_lst)
    print(f'#{test_case}', max(total_lst))