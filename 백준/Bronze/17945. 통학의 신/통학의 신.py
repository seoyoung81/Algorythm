A, B = map(int, input().split())
lst = []

for i in range(-1000, 1001):
    if (i*i + 2*A*i + B) == 0:
        lst.append(i)
    if len(lst) == 2:
        break

print(*lst)