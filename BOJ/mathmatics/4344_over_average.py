T = int(input())    # test case
for test_case in range(1, T+1):
    score_list = list(map(int, input().split()))    # score_list[0]: 학생 수, student score
    # average
    total = 0
    for score in score_list:
        total += score
    # except first index
    total = total - score_list[0]
    average = total / score_list[0]
    # print(average)

    # count student
    cnt = 0
    for i in range(1, score_list[0]+1):
        if score_list[i] > average:
            cnt += 1

    # get percentage
    percentage = round((cnt / (len(score_list) - 1)) * 100, 3)
    print(f'{percentage:.3f}%') # 소수점 세자리 수 표현 방법


