def solution(before, after):
    answer = 0
    before = list(before)
    after = list(after)
    before.sort()
    after.sort()
    
    if before == after:
        answer = 1
    
    return answer