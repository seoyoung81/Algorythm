arr = [list(map(str, input().split())) for _ in range(10)]
paper = []
rec = [0] * 6   # cnt
# bruteforce
for i in range(10):
    paper.append(''.join(arr[i]))

# 전체 탐색
for i in range(10):
    for j in range(10):
        if arr[i][j] == 1:
            count = 0
            if j < 5:
                if arr[i][j:j+5] == '11111':
                    for k in range(1, 4):
                        if arr[i+k][j:j+5] == '11111':
                            count += 1
                        else:
                            print(k)
                            break
                    if count == 4:
                        rec[5] += 1



