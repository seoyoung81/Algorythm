def solution(A, B):
    answer = -1
    A = list(A)
    B = list(B)
    m = len(A)
    
    for i in range(m):
        if A[i] == B[0]:
            if A[i:] + A[:i] == B[:]:
                answer = m - i
            
    
    if answer == m:
        answer = 0
    return answer