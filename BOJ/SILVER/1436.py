N = int(input())    # N 번째 영화의 제목에 들어간 수 구하기

numbers = [str(i) for i in range(10000)]
end_numbers = []
for num in numbers:
    for i in range(len(num)+1):
        num_lst = list(num)
        num_lst.insert(i, '666')
        a = ''.join(num_lst)
        end_numbers.append(int(a))

end_numbers.sort()

for i in range(len(end_numbers)-1):
    if end_numbers[i] == end_numbers[i+1]:
        end_numbers[i] = 0

while end_numbers.count(0) != 0:
    end_numbers.remove(0)

print(end_numbers)
print(end_numbers[N-2])

