T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N x N arr, M x M 파리채
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):  # M 줄 반복
                total += sum(arr[i+k][j:j+M])

            result = max(result, total)

    print(f'#{test_case}', result)