height = []
for _ in range(9):
    height.append(int(input()))   # 난쟁이 키 입력 9명 리스트에 추가

cur = sum(height)   # 전체 키의 합
fake1 = fake2 = 0
for i in range(9):
    for j in range(i+1, 9):
        if height[i] + height[j] == sum(height) - 100:  # 2 명을 제외한 합이 100이라면
            fake1 = height[i]
            fake2 = height[j]
            break

height.remove(fake1)    # 인덱스 오류 없이 리스트의 값을 제거 하고 싶을 때
height.remove(fake2)

sorted_short = sorted(height)

for i in range(7):
    print(sorted_short[i])
