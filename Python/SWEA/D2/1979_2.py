T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())    # N x N , 단어의 길이 K
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    col_puzzle = list(map(list, zip(*puzzle)))  # trans arr

    cnt = 0
    i = 0
    for lst in puzzle:
