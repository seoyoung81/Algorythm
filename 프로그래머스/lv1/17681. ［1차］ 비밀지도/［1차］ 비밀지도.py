def solution(n, arr1, arr2):
    answer = [''] * n
    for i in range(n):
        a = bin(arr1[i])
        b = bin(arr2[i])
        if len(a) != n+2:
            _a = '0' * (n+2-len(a)) + a[2:]
        else:
            _a = a[2:]
        if len(b) != n+2:
            _b = '0' * (n+2-len(b)) + b[2:]
        else:
            _b = b[2:]
  
        for j in range(n):
            if _a[j] == '0' and _b[j] == '0':
                answer[i] += ' '
            else:
               answer[i] += '#'
    return answer