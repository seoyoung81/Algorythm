def solution(s, n):
    answer = ''
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for alpha in s:
        if alpha == ' ':
            answer += ' '
        if alpha.islower():
            print('소문자', alpha)
            for i in range(26):
                if alpha == lower_list[i]:
                    answer += lower_list[(i + n) % 26]
        else:
            print('대문자', alpha)
            for i in range(26):
                if alpha == upper_list[i]:
                    answer += upper_list[(i + n) % 26]
    return answer