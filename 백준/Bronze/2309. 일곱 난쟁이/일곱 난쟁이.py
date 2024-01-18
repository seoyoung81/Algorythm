numbers = []
for _ in range(9):
    n = int(input())
    numbers.append(n)

numbers.sort()
# 7개의 숫자의 합이 100이 되는 것을 찾아 오름차순으로 출력하기
sum_ = sum(numbers)
sum_two = sum_ - 100
s = 0
e = 8
while s < e:
    if numbers[s] + numbers[e] == sum_two:
        numbers.remove(numbers[e])
        numbers.remove(numbers[s])
        break
    elif numbers[s] + numbers[e] < sum_two:
        s += 1
    else:
        e -= 1

for i in range(7):
    print(numbers[i])