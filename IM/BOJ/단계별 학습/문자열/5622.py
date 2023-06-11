number_list = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

number = (str(input())).lower()

num_list = []

for i in range(len(number)):
    for j in range(8):
        if number[i] in number_list[j]:
            num_list.append(j+2)    # 인덱스 위치 + 2
            
# print(num_list)

for i in range(len(num_list)):  # 1은 2초 2는 3초
    num_list[i] = num_list[i] + 1
    
time = sum(num_list)
print(time)