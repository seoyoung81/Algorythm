def solution(s):
    answer = ''
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = []
    for char in s:
        if char.isdecimal():
            answer += str(char)
        else:
            num.append(char)
            for i in range(10):
                if ''.join(num) == number[i]:
                    answer += str(i)
                    num = []
                    break
                    
    return int(answer)