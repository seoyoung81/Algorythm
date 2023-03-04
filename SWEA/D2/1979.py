T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())    # N x N , 단어의 길이 K
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    col_puzzle = list(map(list, zip(*puzzle)))  # trans arr

    cnt = 0     # 단어 넣을 수 있는 자리 세기
    for lst in puzzle:
        for i in range(N-K+1):
            if lst[i:i+K] == [1] * K:   # 일단 단어를 넣을 수 있는 곳이라면
                if i == 0:  # 시작이 0 열이라면
                    if lst[i+K] == 0:   # K+1 번째 열이 1인 경우
                        cnt += 1
                elif i+K-1 == N-1:  # 마지막 열이 N-1 열이라면
                    if lst[i-1] == 0:
                        cnt += 1
                else:
                    if lst[i-1] == 0 and lst[i+K] == 0:
                        cnt += 1


    # print(cnt)

    # 세로 판단
    for lst in col_puzzle:
        for i in range(N-K+1):
            if lst[i:i+K] == [1] * K:   # 일단 단어를 넣을 수 있는 곳이라면
                if i == 0:  # 시작이 0 열이라면
                    if lst[i+K] == 0:   # K+1 번째 열이 1인 경우
                        cnt += 1
                elif i+K-1 == N-1:  # 마지막 열이 N-1 열이라면
                    if lst[i-1] == 0:
                        cnt += 1
                else:
                    if lst[i-1] == 0 and lst[i+K] == 0:
                        cnt += 1

    print(f'#{test_case}', cnt)

