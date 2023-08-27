def solution(d, budget):
    d = sorted(d)
    answer = 0
    if sum(d) <= budget:
        answer = len(d)
    else:
        sum_value = sum(d[:len(d)//2])
        if sum_value < budget:
            print('예산보다 적은 경우')
            for i in range(len(d)//2, len(d)-1):
                sum_value += d[i]
                if sum_value == budget:
                    answer = i+1
                    break
                elif sum_value > budget:
                    answer = i
                    break
        else:
            sum_value = 0
            for i in range(len(d)):
                sum_value += d[i]
                if sum_value == budget:
                    answer = i+1
                    break
                elif sum_value > budget:
                    answer = i
                    break
    return answer




