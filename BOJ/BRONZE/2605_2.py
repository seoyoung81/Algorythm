N = int(input())    # 학생수 <= 100
numbers = list(map(int, input().split()))   # 학생들이 뽑은 번호

line = []     # 1번 넣기

for i in range(N):
    line.insert(i-numbers[i], i+1)

print(*line)
