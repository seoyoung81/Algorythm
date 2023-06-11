S = list(str(input()))   # 단어 입력
# print(S)
from string import ascii_lowercase
alpha_list = list(ascii_lowercase)

index_list = [0] * 26
for i in range(len(alpha_list)):
    if alpha_list[i] not in S:
        index_list[i] = -1
    for j in range(len(S)):
        if alpha_list[i] in S[j]:
            index_list[i] = int(j)
            break

for number in index_list:
    print(number, end = ' ')