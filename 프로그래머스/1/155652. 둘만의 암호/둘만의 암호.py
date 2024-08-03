def solution(s, skip, index):
    answer = ''
    alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # skip 제거
    alpa = [char for char in alpa if char not in skip]
    
    # result 구하기
    for str in s:
        answer += alpa[(alpa.index(str) + index) % len(alpa)]
            
    return answer