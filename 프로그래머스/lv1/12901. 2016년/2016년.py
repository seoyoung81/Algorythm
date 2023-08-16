def solution(a, b):
    answer = ''
    
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    sum = b-1
    for i in range(a-1):
        sum += month[i]
   
    sum %= 7
    answer = day[sum]
    return answer
