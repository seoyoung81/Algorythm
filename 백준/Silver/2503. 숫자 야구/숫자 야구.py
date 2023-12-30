from itertools import permutations

N = int(input())    # 민혁이가 영수에게 질문한 횟수
option = list(permutations((1,2, 3, 4, 5, 6, 7, 8, 9), 3))

for _ in range(N):
    number, strike, ball = map(int, input().split())
    number = list(str(number))
    remove = 0

    for i in range(len(option)):
        strike_cnt, ball_cnt = 0, 0
        i -= remove
        for j in range(3):
            number[j] = int(number[j])
            if number[j] in option[i]:
                if j == option[i].index(number[j]):
                    strike_cnt += 1
                else:
                    ball_cnt +=  1
        if strike != strike_cnt or ball != ball_cnt:
            option.remove(option[i])
            remove += 1
print(len(option))