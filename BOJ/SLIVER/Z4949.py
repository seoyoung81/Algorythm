bracket = str(map(str, input().split()))    # 문자열 입력받기
# 온점이면 끝나고 다시 한다는 걸 못 하겟음
stack = []
for string in bracket:
    while string != '.':
        if string == '(' or string == ')' or string == '[' or string == ']':
            if not stack:   # empty stack
                stack.append(string)
            else:   # not empty stack
                if string == '(' or string =='[':
                    stack.append(string)
                elif string == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(string)
                elif string == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(string)

    if stack:
        print('NO')
    else:
        print('YES')