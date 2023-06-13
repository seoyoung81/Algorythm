def solution(id_pw, db):
    answer = ''
    id_lst = []
    for i in db:
        id_lst.append(i[0])
    
    if id_pw in db:
        answer = 'login'
    elif id_pw[0] in id_lst:
        answer = 'wrong pw'
    else:
        answer = 'fail'

    return answer