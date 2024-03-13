def solution(brown, yellow):
    answer = []
    for i in range(1, (brown-4)//2):
        if i*((brown-4)//2-i) == yellow:
            answer.append(i+2)
            answer.append((brown-4)//2-i+2) 
            break
    answer = sorted(answer, reverse=True)
    return answer