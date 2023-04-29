import sys
sys.stdin = open('input.txt')

# 1 N극 / 2 S극
T = 10
for test_case in range(1, T + 1):
    N = int(input())    # 정사각형 한 변의 길이 = 100
    table = [list(map(int, input().split())) for _ in range(N)]
    col_table = list(map(list, zip(*table)))    # 전치(행에서 생각하는게 더 편함)

    # 0 삭제 하기
    for lst in col_table:
        while 0 in lst:
            lst.remove(0)
    # print(col_table)

    # N극 S극으로 끌려가는 자성체 제거
    for lst in col_table:
        while lst[0] == 2:  # 가장 첫번째 원소가 2라면 N 극으로 끌려간다
            lst.pop(0)
        while lst[-1] == 1: # 가장 마지막 원소가 1이라면 S 극으로 끌려간다
            lst.pop()

    # print(col_table)


    magnetic = 0
    for lst in col_table:
        idx = 0     # idx 는 행의 끝까지 돌기
        m = len(lst)
        while idx != m:     # 1이면 2 나올 때까지 반복 / 2나오면 1나올때까지 반복
            if lst[idx] == 1:
                idx += 1    # 다음 확인
                while lst[idx] != 2:    # 2 나올 때까지 반복
                    idx += 1

                magnetic += 1       # 2가 나옴 -> 교착 1개 생김
                idx += 1            # 다음 인덱스

            elif lst[idx] == 2:     # 2이면 전 단계가 2일테니까 그냥 pass
                idx += 1
    
    print(f'#{test_case}', magnetic)