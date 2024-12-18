N = str(input())
set = [0] * 10

for char in N:
  set[int(char)] += 1

sum_value =(set[6] + set[9]+1) // 2
set[6] = sum_value
set[9] = sum_value

print(max(set))