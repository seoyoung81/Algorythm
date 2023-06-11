n = int(input())    # 수열의 크기
numbers = list(map(int, input().split()))   # 수열에 포함되는 수
x = int(input())    # 두 수의 합이 x

# cnt = 0     # 조건을 만족하는 쌍의 개수 세기
# for i in range(n):
#     for j in range(i+1, n):
#         if numbers[i] + numbers[j] == x: # 두 수의 합이 x라면
#             cnt += 1     # 한 개 세주기
#             break
#
#
# print(cnt)

cnt = 0
for num in numbers:
    if x - num in numbers:
        cnt += 1

print(cnt//2)