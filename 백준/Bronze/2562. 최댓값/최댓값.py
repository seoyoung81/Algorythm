numbers = []
for _ in range(9):
    numbers.append(int(input()))

result = 0
result_num = 0
for i in range(9):
    if result_num < numbers[i]:
        result = i+1
        result_num = numbers[i]

print(result_num)
print(result)