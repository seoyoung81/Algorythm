N, K = map(int, input().split())    # 학생 수, 한 방에 배정할 수 있는 최대 인원 수
girls = [0] * 7  # 여학생 담을 리스트
boys = [0] * 7  # 남학생 담을 리스트
# 여자 0 남자 1
for _ in range(N):  # N 명의 학생정보 입력받기
    gender, grade = map(int, input().split())   # 성별, 학년
    # 여자인 경우
    if gender == 0:
        girls[grade] += 1   # 학년 index에 1명 추가
    else:   # 남자인 경우
        boys[grade] += 1

# print(girls)
# print(boys)

# 학생 수를 방 배정 인원으로 나눈 몫 만큼 방이 필요
cnt = 0
for student in girls:
    if student % K == 0:  # 나누어 떨어지면
        cnt += student // K
    else:   # 나누어 떨어지지 않으면
        cnt += student // K + 1
# print(cnt)

for student in boys:
    if student % K == 0:  # 나누어 떨어지면
        cnt += student // K
    else:   # 나누어 떨어지지 않으면
        cnt += student // K + 1


print(cnt)
