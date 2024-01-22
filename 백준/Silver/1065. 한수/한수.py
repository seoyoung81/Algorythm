def one_number(n):
    if n < 100:
        return True
    numbers = list(str(n))
    for i in range(1, len(numbers)-1):
        if int(numbers[i+1]) - int(numbers[i]) != int(numbers[i]) - int(numbers[i-1]):
            return False
    return True

n = int(input())
result = 0
for i in range(1, n+1):
    if one_number(i):
        result += 1
print(result)

