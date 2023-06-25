def solution(s):
    answer = False
    m = len(s)
    if m == 4 or m == 6:
        for char in s:
            if not char.isdecimal():
                answer = False
                break
            answer = True
    return answer