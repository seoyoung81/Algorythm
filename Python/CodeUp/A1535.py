n = int(input())
numbers = list(map(int, input().split()))
# print(numbers)

def max_func():
    count = 0
    max_1 = numbers[0]
    for i in range(n):
        if max_1 < numbers[i]:
            max_1 = numbers[i]
            count = i
    return count + 1

print(max_func())




