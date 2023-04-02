T = int(input())
for test_case in range(1, T + 1):
    two = input()
    three = input()

    numbers = []
    result = 0
    for i in range(1, len(two)):    # 앞자리는 무조건 1
        original = list(two)
        if two[i] == '0':
            original[i] = '1'
        else:
            original[i] = '0'
        numbers.append(int(''.join(original), 2))
    # print(numbers)


    A = ['0', '1', '2']
    for i in range(len(three)):
        for j in A:
            original = list(three)
            if three[i] != j:
                original[i] = j
                original = int(''.join(original), 3)
                if original in numbers:
                    print(f'#{test_case}', original)
                    break






