lst = list(map(int, input().split()))

room = sorted(lst[:3], reverse=True)
student = lst[3]
for bed in room:
    student %= bed

if student == 0:
    print(1)
else:
    print(0)