N = int(input())    # 시험 본 과목의 개수
score_list = list(map(int, input().split())) # 원래 성적
max_subject = max(score_list)    # 최고점

new_score = []  # 새로운 점수를 리스트에 추가
for score in score_list:    # 점수리스트에 있는 점수들에 대해서
    new_score.append(score/max_subject*100) # 새로운 점수는 최댓값으로 나누고 100을 곱한 것

total = sum(new_score)  # 합계
print(total/N)  # 평균 출력