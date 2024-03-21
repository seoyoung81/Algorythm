from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    n = len(dungeons)
    for permute in permutations(dungeons, n):
        piro = k
        count = 0
        for perm in permute:
            if piro >= perm[0]:
                piro -= perm[1]
                count += 1
            if count > answer:
                answer = count  
            if count == n:
                answer = count
                break
        
    return answer