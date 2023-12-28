numbers = list(map(int, input().split()))
min_number = min(numbers)
result = 0

for i in range(min_number, 100**3+1):
    count = 0
    for num in numbers:
        if i % num == 0:
            count += 1

    if count >= 3:
        result = i
        break

print(result)