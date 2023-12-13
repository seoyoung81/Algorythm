N = int(input())
result = 0
for i in range(1, 501):
    for j in range(i+1, 501):
        if (i*i + N) == j*j:
            result += 1
print(result)