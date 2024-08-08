r = [0] * 42
for _ in range(10):
    num = int(input())
    r[num%42] = 1

result = r.count(1)
print(result)