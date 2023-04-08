T = int(input())
for _ in range(T):
    N, M = map(int, input().split())    # 문서의 개수, 궁금한 문서의 인덱스 값
    important = list(map(int, input().split()))     # 문서의 중요도
    idx = [i for i in range(N)]
    idx[M] = 'target'

    # 순서
    order = 0

    while True:
        if important[0] == max(important):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                important.pop(0)
                idx.pop(0)
        else:
            important.append(important.pop(0))
            idx.append(idx.pop(0))


