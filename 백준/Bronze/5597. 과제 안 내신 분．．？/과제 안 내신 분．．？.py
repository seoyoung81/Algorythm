numbers = [0] * 31

for _ in range(28):
    numbers[int(input())] = 1

for i in range(1, 31):
    if numbers[i] == 0:
        print(i)

