# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # 전체크기, 파리채 크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # N x N 2차원 리스트


    fly_list = []
    for j in range(N-M+2):
        for i in range(N-M+1):
            fly_list.append(arr[j][i:i+M])
    # print(fly_list)
    total = [0] * len(fly_list)
    for i in range(21):    # 24개
        total[i] = fly_list[i] + fly_list[i+N-1]
    print(total)
