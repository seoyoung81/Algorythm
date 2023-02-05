string = str(input()).lower()  # 문자를 입력받고, 소문자로 바꿔주기

count = {}          # 빈 딕셔너리 
for str in string:  # 입력받은 문자열의 문자에 대하여
    try:
        count[str] += 1
    except:
        count[str] = 1      # 어떤 문자가 몇 개 있는지 딕셔너리 출력
    
count_list = sorted(count.values())     # value 값들을 오름차순으로 정렬
max_number = count_list[-1]             # 가장 큰 값은 마지막 요소

for i in count_list:                    # value 값들을 정렬한 리스트에 대하여
    if len(count_list) == 1:            # count_list 가 1개이면 
        print(string.upper())           # 문자가 1개이니까 그냥 strig을 대문자로 바꿔서 출력
        
    elif count_list[-1] == count_list[-2]:  # count_list에서 맨 뒤 값이랑 뒤에서 두번째 값이 같으면 -> 같은 개수인 문자가 존재하므로
        print('?')                          # 물음표 출력
        break                               
    
    else:         # 최대 갯수인 문자가 1개라면
        print(max(count, key = count.get).upper())  # value가 가장 큰 값인 key 값 출력하기!!
    
        break


       