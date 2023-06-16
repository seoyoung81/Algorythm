def solution(board):
    answer = 0
    n = len(board)
    result = [[0]*n for i in range(n)]
    # 완전 탐색
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        np = i + p
                        nq = j + q
                        if 0 <= np < n and 0 <= nq < n:
                            result[np][nq] = 1
    
    for lst in result:
        answer += lst.count(0)
    
    return answer