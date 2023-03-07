M, N = map(int, input().split())    # M x N arr
board = [input() for _ in range(M)]
result = []
# 체스판 8x8 으로 맞추기
for i in range(M-7):
    for j in range(N-7):
        cnt1 = 0
        cnt2 = 0
        for p in range(i, i+8):
            for q in range(j, j+8):

                # 전체 탐색
                # black으로 시작하는 경우
                if p % 2:   # 홀수줄은 white 로 시작
                    if not q % 2:   # 짝수칸이라면
                        if board[p][q] != 'W':
                            cnt1 += 1
                    else:   # 홀수칸이라면
                        if board[p][q] != 'B':
                            cnt1 += 1
                else:   # 짝수줄은 white로 시작 -> 홀수칸 white
                    if q % 2:   # 홀수칸이라면
                        if board[p][q] != 'W':
                            cnt1 += 1
                    else:   # 짝수칸이라면
                        if board[p][q] != 'B':
                            cnt1 += 1


                # white로 시작하는 경우
                if p % 2:   # 홀수 줄에서 1, 3, 5
                    if not q % 2:   # 짝수칸이라면 0, 2, 4
                        if board[p][q] != 'B':
                            cnt2 += 1
                    else:   # 홀수칸이라면
                        if board[p][q] != 'W':
                            cnt2 += 1
                else:   # 짝수줄은 white로 시작 -> 홀수칸 white
                    if q % 2:   # 홀수칸이라면
                        if board[p][q] != 'B':
                            cnt2 += 1
                    else:   # 짝수칸이라면
                        if board[p][q] != 'W':
                            cnt2 += 1
        result.append(cnt1)
        result.append(cnt2)

print(min(result))

