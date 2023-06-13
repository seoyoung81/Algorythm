def solution(spell, dic):
    answer = 2
    for word in dic:
        cnt = 0
        for alpha in spell:
            if not alpha in word:
                pass
            else:
               cnt += 1
        if cnt == len(spell):
            answer = 1   
    return answer