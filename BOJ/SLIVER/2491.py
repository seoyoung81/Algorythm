N = int(input())    # 수열의 길이
numbers = list(map(int, input().split()))   # 수열

cnt_list = [0] * N


for i in range(N-1):
    if numbers[i] <= numbers[i+1]:  # 증가
        cnt_list[i+1] += cnt_list[i] + 1
        if numbers[i-1] >= numbers[i]:
            cnt_list[i] = 0
            cnt_list[i+1] += cnt_list[i] + 1
    elif numbers[i] >= numbers[i+1]:   # 감소
        cnt_list[i] = 1
        cnt_list[i+1] += cnt_list[i] + 1
        if numbers[i-1] <= numbers[i]:
            cnt_list[i] = 0
            cnt_list[i+1] += cnt_list[i] + 1

print(max(cnt_list)-1)
