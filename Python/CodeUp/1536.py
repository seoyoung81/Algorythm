def min():
    min_1 = num_list[0]
    for i in range(n):
        if min_1 > num_list[i]:
            min_1 = num_list[i]
    return min_1
    
    

n = int(input())
num_list = list(map(int, input().split()))
print(min())


# min_1 = num_list[0]
# for i in num_list:
#     if i < min_1:
#         min_1 = i
#     return min_1