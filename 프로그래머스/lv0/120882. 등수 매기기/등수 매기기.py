def solution(score):
    answer = []
    for i in range(len(score)):
        score[i] = ((score[i][0] + score[i][1])/2)
    
    score2 = []
    for num in score:
        score2.append(num)
    score2.sort(reverse=True)
    
    for num1 in score:
        for i in range(len(score2)):
            if num1 == score2[i]:
                answer.append(i+1)
                break
  
    return answer