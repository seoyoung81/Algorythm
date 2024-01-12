import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = list(map(int, input().split()))

# 누적합 딕셔너리
sum_dict = {0: 1}

sum_ = 0
answer = 0

for i in number:
    sum_ += i

    # 현재까지 누적합 중에서 누적합 - (이전 누적합) = k 가 있으면
    if sum_ - K in sum_dict.keys():
        answer += sum_dict[sum_-K]

    # 누적 합 딕셔너리 갱신
    sum_dict[sum_] = sum_dict.get(sum_, 0) + 1

print(answer)