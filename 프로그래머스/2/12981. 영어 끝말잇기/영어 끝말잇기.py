def solution(n, words):
    
    for i in range(1, len(words)):
        #글자가 맞지 않을 때
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    
    return [0,0]