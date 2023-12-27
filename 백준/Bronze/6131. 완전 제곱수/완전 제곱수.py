N = int(input())
square = [i*i for i in range(1, 501)]
count = 0

for i in range(499):
    for j in range(i+1, 500):
        if square[i] + N == square[j]:
            count += 1

print(count)