num = str(input())
number = []
# input 받기
for i in range(len(num)):
    if num[i] != '+' and num[i] != '-':
        if len(number) == 0:    # 비어있으면
            number.append(num[i])
        else:
            if number[-1] == '+' or number[-1] == '-': # 전에가 연산기호라면
                number.append(num[i])
            else:   # 전에가 숫자인 경우만
                number[-1] += num[i]
    else:
        number.append(num[i])
print(number) # ['55', '-', '50', '+', '40']

# # 괄호 넣기
# expression = ['(']
# for i in range(len(number)):
#     if number[i] == '-':
#         expression.append(')')
#         expression.append('-')
#         expression.append('(')
#     else:
#         expression.append(number[i])
# expression.append(')')
# # print(expression) ['(', '55', ')', '-', '(', '50', '+', '40', ')']

# 그냥 무조건 더하기 먼저하기
# ['55', '-', '50', '+', '40']

# plus = []
# i = 0
# while i != len(number):
#     if number[i+1] == '+':
#         plus.append(int(number[i]) + int(number[i+2]))
#         i += 3
#     else:
#         plus.append(number[i])
#         i += 1
# else:
#     if number[i+1] == '+':
#         plus.append(int(number[i]) + int(number[i+2]))
#         i += 3
#
# print(plus)