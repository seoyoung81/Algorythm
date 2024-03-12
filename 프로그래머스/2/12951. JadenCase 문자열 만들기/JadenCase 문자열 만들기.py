def solution(s):
    answer = ''
    result = []
    s = s.lower()
    words = list(s.split(" "))
    
    for char in words:
        if char != "":
            result.append(char[0].upper() + char[1:])
        else:
            result.append("")


    answer = ' '.join(result)
    return answer
