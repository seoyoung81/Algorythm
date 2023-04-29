T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # N번 양 세기
    num = list(map(int, str(N)))
    # 0~9가 전부 등장하면 양 세기 종료 -> 최소 몇 번 양 세야하는지 구하기
    numbers = [0] * 10
    cnt = 0

    K = 2
    while sum(numbers) != 10:   # 모든 숫자가 등장할 때 까지
        for i in range(len(num)):
            numbers[num[i]] = 1

        N = N // (K-1)
        N = N * K
        num = list(map(int, str(N)))
        K += 1


    N = N // (K-1)
    N = N * (K-2)

    print(f'#{test_case}', N)
