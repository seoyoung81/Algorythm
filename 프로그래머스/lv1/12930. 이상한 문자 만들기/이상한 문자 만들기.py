def solution(s):
    answer = ''
    lst = list(str(s).split(' '))
    for word in lst:
        word = list(word)
        for i in range(len(word)):
            if i % 2 == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
        word.append(' ')
        answer += ''.join(word)
      
    return answer[:len(answer)-1]