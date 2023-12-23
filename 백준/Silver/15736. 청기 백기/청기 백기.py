N = int(input())    # 첫번째 출전한 학생의 수, 깃발의 개수
cnt = 0
# 1부터 홀수번 뒤집힌 깃발의 개수 구하기 -> 제곱수 구하기
# 제곱수 리스트
square = [0] * 50000
for i in range(1, N+1):
    square[i] = i*i
    if i*i > N:
        break

for num in square:
    if 1 <= num <= N:
        cnt += 1
print(cnt)



