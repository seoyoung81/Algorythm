T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # 당근의 개수
    carrot = list(map(int, input().split()))

    # 당근 크기 정렬하기
    carrot.sort()

    # 최소 개수 차이
    minV = N    # 차이는 N 보다 작음

    # 당근 리스트를 3구역으로 쪼개기
    for a in range(N-2):    # 첫번째 구역은 0부터 N-3까지 가능
        for b in range(a+1, N-1):   # 두번째 구역은 a+1 부터 N-2까지 가능
            if carrot[a] != carrot[a+1] and carrot[b] != carrot[b+1]:
                A = a + 1   # 소 당근 개수
                B = b - a   # 중 당근 개수
                C = N - 1 - b   # 대 당근 개수
                if A * B * C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:
                    cnt = max(A, B, C) - min(A, B, C)   # 가장 큰 것과 가장 작은 것의 차이.
                    minV = min(minV, cnt)



    if minV == N:   # 당근 나누기에 실패했다면
        minV = -1

    print(f'#{test_case}', minV)

