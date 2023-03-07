N = int(input())    # N 개의 숫자
numbers = list(map(int, input().split()))

increase_lst = [0] * (N+1)
decrease_lst = [0] * (N+1)

for i in range(N-1):
    if numbers[i] <= numbers[i+1]:  # 증가하면
        increase_lst[i+1] += increase_lst[i] + 1
        if numbers[i] == numbers[i+1]:
            decrease_lst[i + 1] += decrease_lst[i] + 1
    elif numbers[i] >= numbers[i+1]:    # 감소하면
        decrease_lst[i+1] += decrease_lst[i] + 1
        if numbers[i] == numbers[i + 1]:
            increase_lst[i + 1] += increase_lst[i] + 1

# 최댓값 구하기
a = max(increase_lst)
b = max(decrease_lst)
print(max(a, b) + 1)