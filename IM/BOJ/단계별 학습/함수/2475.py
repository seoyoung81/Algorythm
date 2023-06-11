def KOI(numbers):
    num_list = list(numbers)
    sum = 0
    for x in num_list:
        sum += int(x) * int(x)
    number = sum % 10
    return number

numbers = list(input().split())
print(KOI(numbers))