def solution(sizes):
    answer = 0
    width = 0
    height = 0
    
    wallet = []
    for lst in sizes:
        wallet.append(sorted(lst, reverse=True))
    
    wallet = sorted(wallet, reverse=True)
    
    width = wallet[0][0]
    height = wallet[0][1]
    for lst in wallet:
       if lst[1] > height:
            height = lst[1]
            
    answer = width*height
    
    return answer