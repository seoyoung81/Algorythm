maxV = 0
l = 0
c = 0

for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        n = arr[j]
        if n >= maxV:
            maxV = n
            l = i+1
            c = j+1

print(maxV)
print(l, c)