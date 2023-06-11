'''
입력 순서 A, B, C, D, E, F
짝 A F / B D / C E
'''
N = int(input())    # 주사위 개수
numbers = [list(map(int, input().split())) for _ in range(N)]

total = 0
reverse = [5, 3, 4, 1, 2, 0]        # 0번 인덱스에 짝 5, 1번 인덱스에 짝 3, 2번 리스트에 짝 4
for floor in range(1, 7):
    sum = 0
    for lst in numbers:
        top = lst[reverse[lst.index(floor)]]
        if floor + top == 11:   # 위 아래가 5, 6인 경우
            sum += 4
        elif floor == 6 or top == 6:    # 6 이 한 번이라도 쓰인 경우
            sum += 5
        else:
            sum += 6                    # 6 이 한 번도 안 쓰인 경우
        floor = top
    if sum > total:
        total = sum
print(total)



