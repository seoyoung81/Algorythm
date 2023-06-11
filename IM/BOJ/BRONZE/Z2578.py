bingo_list = []
for i in range(5):
    a = list(map(int, input().split()))     # a를 5줄 입력받고
    bingo_list.append(a)                    # 5X5 2차원리스트 생성
# print(bingo_list)

                                  
mc_list = []
for i in range(5):
    b = list(map(int, input().split()))     # b를 5줄 입력받고
    for j in b:
        mc_list.append(b)                       
for idx, num in enumerate(mc_list):                      
    for m in bingo_list:            # 첫번째 줄부터 차례대로 확인
        if num in m:                # 부르는 숫자가 해당 줄에 있으면 
            m[m.index(num)] = 0     # 숫자를 0으로 변환
            break
# print(bingo_list)
print(mc_list)
        
# 빙고 세기 

count = 0
for l in bingo_list:
    if l.count(0) == 5:
        count += 1

for j in range(5):
    y = 0
    for j in range(5):
        if bingo_list[j][i] == 0:
            y += 1
        if y == 5:
            count += 1

       
if bingo_list[0][4] + bingo_list[1][3] + bingo_list[2][3] + bingo_list[3][2] + bingo_list[4][0] == 0:
    count += 1
    
if bingo_list[0][0] + bingo_list[1][1] + bingo_list[2][2] + bingo_list[3][3] + bingo_list[4][4] == 0:
    count += 1

            
if count >= 3:
    print(count)
    



