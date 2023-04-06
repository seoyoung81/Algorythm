while True:
    s = input()
    result = ''
    if s == '.':
        break

    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                result = 'no'
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = 'no'
                    break
        elif i == '[':
            stack.append('[')
        elif i == ']':
            if len(stack) == 0:
                result = 'no'
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    result = 'no'

    if stack or result == 'no':
        print('no')
    else:
        print('yes')





