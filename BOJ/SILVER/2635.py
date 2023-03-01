N = int(input())

if N <= 2:
    memo = [0] * (N*N*N+1)
else:
    memo = [0] * (N*2 + 1)

memo[0] = N

numbers = []
# 두번째 숫자 정하기
for i in range(N+1):
    memo[1] = i
    # 다음 숫자들 정하기
    for j in range(2, len(memo)):
        memo[j] = memo[j-2] - memo[j-1]

        # 음수가 되는 순간
        if memo[j] < 0:
            numbers.append(memo[:j])
            break

# print(numbers)

if N == 1:
    numbers = [[1, 1, 0, 1]]

# 가장 길이가 긴 리스트 찾기
max_lst = numbers[0]
for lst in numbers:
    if len(max_lst) < len(lst): # 길이가 더 긴 리스트가 있다면
        max_lst = lst

print(len(max_lst))
print(*max_lst)


