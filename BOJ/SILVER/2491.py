N = int(input())    # 수열의 길이
numbers = list(map(int, input().split()))   # 수열

cnt_list = [[0] * (N+1), [0] * (N+1)]
# print(cnt_list)


for i in range(N-1):
    if numbers[i] < numbers[i+1]:  # 증가
        cnt_list[0][i+1] += cnt_list[0][i] + 1  # 증가 정보만 담아서 count 세기

    elif numbers[i] > numbers[i+1]:   # 감소
        cnt_list[1][i+1] += cnt_list[1][i] + 1  # 감소 정보만 담아서 count 세리

    else:       # 변화가 없는 경우
        cnt_list[0][i + 1] += cnt_list[0][i] + 1
        cnt_list[1][i + 1] += cnt_list[1][i] + 1

a = max(cnt_list[0])
b = max(cnt_list[1])

if a >= b:
    print(a+1)
else:
    print(b+1)
