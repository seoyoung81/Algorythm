mario = []
result = 0
for i in range(10):
    mario.append(int(input()))
for j in mario:
    result += j
    if result >= 100:
        if result - 100 > 100 - (result - j):
            result -= j
        break
print(result)