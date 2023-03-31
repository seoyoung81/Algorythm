'''
T = int(input())
N, K = map(int, input().split())    # N 개의 자연수에서 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수
A = list(map(int, input().split())) # N 개의 자연수 수열

# 모든 경우의 수를 구해보자 -> 부분집합
for test_case in range(1, T + 1):
    lst = [[] for _ in range(1<<N)]

    for i in range(0, (1<<N)):
        for j in range(0, N):
            if i & (1<<j):
                lst[i].append(A[j])

    cnt = 0
    for subset in lst:
        if sum(subset) == K:
           cnt += 1

    print(f'#{test_case}', cnt)
'''

def dfs(n, sm):
    global ans
    # [3] 가지치기: 더 이상 정답 갱신 가능성이 없는 경우
    # 가장 마지막에, 가장 위쪽에
    if K < sm:
        return

    # [1] 종료 조건(n에 관련): 반드시 정답처리는 여기서만
    if n == N:
        if sm == K:
            ans += 1
        return

    # [2] 하부호출
    dfs(n+1, sm + lst[n])   # 포함
    dfs(n+1, sm)            # 포함 X


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)

    print(f'#{test_case}', ans)