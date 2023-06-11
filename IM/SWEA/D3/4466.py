T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())    # N 개 시험, K 개 선택
    scores = sorted(list(map(int, input().split())), reverse=True)    # 시험 점수 정렬 시키기

    total = 0
    for i in range(K):
        total += scores[i]

    print(f'#{test_case}', total)
