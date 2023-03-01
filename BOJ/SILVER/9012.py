T = int(input())    # test case
for test_case in range(1, T + 1):
    bracket = str(input())

    stack = []
    for string in bracket:
        if not stack:   # empty stack
            stack.append(string)    # push
        else:           # not empty stack
            if string == '(':
                stack.append(string)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(string)

    if stack:
        print("NO")
    else:
        print("YES")



