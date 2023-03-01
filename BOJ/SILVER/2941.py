croatia = str(input())
croatia_list = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

m = len(croatia)
cnt = m
i = 0
while i <= m - 1:   # i가 문자열의 길이보다 작을 동안 반복
    if croatia[i:i+3] == 'dz=':     # 3글자 연속인 것이 'dz=' 라면
        cnt -= 2    # 개수에서는 2개를 빼주고
        i += 3      # 문자열은 3개를 건너 뛴다
    elif croatia[i:i+2] in croatia_list:    # 2글자 연속인 것이 크로아티아 리스트에 있다면
        cnt -= 1    # 개수는 1개를 빼주고
        i += 2      # 문자열은 2개를 건너 뛴다
    else:           # 위 경우에 해당하지 않는다면
        i += 1      # 그냥 1개만 건너뛴다


print(cnt)