from string import ascii_lowercase

def solution(age):
    answer = ''
    alpha_list = list(ascii_lowercase)
    age = list(str(age))
    
    for num in age:
        answer += alpha_list[int(num)]
    return answer