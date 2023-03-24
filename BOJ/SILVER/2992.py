import itertools    # permutations

X = list(map(str, input()))
x_number = int(''.join(X))

lst = list(itertools.permutations(X, len(X)))
# print(lst) [('1', '5', '6'), ('1', '6', '5'), ('5', '1', '6'), ('5', '6', '1'), ('6', '1', '5'), ('6', '5', '1')]

number_lst = []
for tupl in list(lst):
    number = ''
    for i in range(len(X)):
        number += tupl[i]
    if int(number) > x_number:
        number_lst.append(int(number))

if len(number_lst) == 0:
    print(0)
else:
    print(sorted(number_lst)[0])


