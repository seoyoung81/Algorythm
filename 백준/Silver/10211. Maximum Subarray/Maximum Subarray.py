t = int(input())
for test_case in range(t):
  n = int(input())
  number = list(map(int, input().split()))

  sum_lst = [0] * n
  sum_lst[0] = number[0]
  for i in range(1, n):
    sum_lst[i] = max(number[i] + sum_lst[i-1], number[i])

  print(max(sum_lst))