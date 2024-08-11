arr = []

for i in range(5):
    lst = (list(map(str, input())))
    arr.append(lst + (15-len(lst))*[10])



result = ''
for i in range(15):
    for j in range(5):
        if arr[j][i] != 10:
            result += arr[j][i]

print(result)
