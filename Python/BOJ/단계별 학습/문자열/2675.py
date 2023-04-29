T = int(input())    # 테스트 케이스 개수

for _ in range(T):
    R, S = input().split()

    str_list = []
    for str in S:
        str_list.append(str*int(R))    

    for i in range(len(str_list)):
        print(str_list[i], end = '')
    print()     # 다음 줄 입력이 안 될 대 넣어보자!!
