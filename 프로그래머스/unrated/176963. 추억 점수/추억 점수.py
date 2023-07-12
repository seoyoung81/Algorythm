def solution(name, yearning, photo):
    answer = [0] * len(photo)
    for i in range(len(photo)):
        photo_lst = set(photo[i])
        for photo_name in photo_lst:
            for j in range(len(name)):
                if photo_name == name[j]:
                    answer[i] += yearning[j] 
                    break
    return answer