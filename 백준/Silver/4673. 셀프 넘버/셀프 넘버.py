numbers = [1 for i in range(20001)]

for i in range(1, 10001):
    sum = i
    a = list(str(i))
    for num in a:
        sum += int(num)
    
    numbers[sum] = 0

for i in range(1, 10001):
    if numbers[i] == 1:
        print(i)
