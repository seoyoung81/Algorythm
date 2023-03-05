switch = list(map(str, input()))    # 전구 상태
switch.insert(0, 'N')
# print(switch)
# Y : 켜 있는 경우 N : 꺼져 있는 경우
N = len(switch)-1 # 전구 개수

# 처음부터 다 꺼진 경우
if switch == ['N'] * (N+1):
    print(0)
else:
    cnt = 0
    for i in range(1, N+1):
        if switch[i] == 'Y':  # 켜져 있으면
            cnt += 1
            for j in range(1, N+1):
                if j % i == 0:
                    if switch[j] == 'N':
                        switch[j] = 'Y'
                    else:
                        switch[j] = 'N'

        if switch == ['N'] * (N+1):
            print(cnt)
            break
    else:
        # 다 못끄는 경우
        print(-1)





