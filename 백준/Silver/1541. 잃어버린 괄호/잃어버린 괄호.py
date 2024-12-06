lst = list(map(str, input().split('-')))
number = []
for char in lst:
  a = list(map(int, char.split('+')))
  number.append(sum(a))

result = number[0]
for i in range(1, len(number)):
  result -= number[i]

print(result)