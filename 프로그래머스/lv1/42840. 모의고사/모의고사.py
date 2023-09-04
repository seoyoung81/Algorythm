def solution(answers):
    result = []
    answer = [0] * 3
    array1 = [1, 2, 3, 4, 5] * 2000
    array2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    array3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    for i in range(len(answers)):
        if answers[i] == array1[i]:
            answer[0] += 1
        if answers[i] == array2[i]:
            answer[1] += 1
        if answers[i] == array3[i]:
            answer[2] += 1
    
    maxV = max(answer)
    for i in range(3):
        if maxV == answer[i]:
            result.append(i+1)
    return result