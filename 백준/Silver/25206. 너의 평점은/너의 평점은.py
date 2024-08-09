grade_lst = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
sum = 0
subject_cnt = 0

for _ in range(20):
    subject, credit, grade = map(str, input().split())
    if grade != 'P':
        sum += float(credit) * score[grade_lst.index(grade)]
        subject_cnt += float(credit)

print(sum/subject_cnt)