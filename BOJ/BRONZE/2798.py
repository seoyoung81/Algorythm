N, M = map(int, input().split())    # N 장의 카드, 최대 합 M에 가깞게 만들기
numbers = list(map(int, input().split()))

total_lst = []

# 3개씩 합 중에서 M 보다 같거나 작은 것들만
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = 0
            total += numbers[i]
            total += numbers[j]
            total += numbers[k]

            if total <= M:
                total_lst.append(total)

# 그 중에서 가장 큰 값
print(max(total_lst))