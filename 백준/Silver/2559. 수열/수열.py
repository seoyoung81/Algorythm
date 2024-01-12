N, K = map(int, input().split()) # 총 개수, 연속의 개수
numbers = list(map(int, input().split()))

# 슬라이딩 윈도우
# 시간 초과
# lst = numbers[:K]
# total = [sum(lst)]
# for i in range(K, N):
#     lst.pop(0)          # 제일 앞에 꺼 빼고
#     lst.append(numbers[i])      # 다음 꺼 더해주기
#     total.append(sum(lst))
#
#
# print(max(total))

total_lst = [sum(numbers[:K])]
total = sum(numbers[:K])
for i in range(N-K):
    total -= numbers[i]
    total += numbers[i+K]
    total_lst.append(total)

print(max(total_lst))

