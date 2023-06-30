def solution(s):
    answer = []
    stack = []
    for char in s:
        if not char in stack:
            answer.append(-1)
            stack.append(char)
        else:
            for i in range(len(stack)-1, -1, -1):
                if stack[i] == char:
                    answer.append(len(stack)-i)
                    break
            stack.append(char)
    return answer