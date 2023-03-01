K = int(input())
stack = []
for _ in range(K):  # K 만큼 반복
    number = int(input())
    if number == 0:     # 입력된 숫자가 0 이라면
        stack.pop()     # 가장 최근에 쓴 수를 지우기
    else:               # 0 이 아니라면
        stack.append(number)    # stack에 push

print(sum(stack))
