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