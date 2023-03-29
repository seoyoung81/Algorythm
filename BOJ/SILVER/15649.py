N, M = map(int, input().split())
# 3, 1
# 1부터 3까지 자연수 중에서 중복없이 1개 고르기 -> 1, 2, 3
# 4, 2
# 1부터 4까지 자연수 중에서 중복없이 2개 고르기 -> 12 13 14 21 23 24 31 32 34 41 42 43
lst = []

def dfs():
    if len(lst) == M:   # M개가 되면 출
        print(*lst)
        return

    for i in range(1, N+1): # 1부터 N 까
        if i not in lst:    # 리스트에 i 가 없으면
            lst.append(i)   # i 추가
            dfs()
            lst.pop()   # 하나 제거
            # 1 -> 12 -> 1 -> 13 -> 1 -> 14 ->

dfs()
