N = int(input())
result = 0
for _ in range(N):
    word = list(str(input()))
    new_word = [word[0]]
    for i in range(1, len(word)):
        if (word[i] != word[i-1]):
            new_word.append(word[i])
    
    if len(set(new_word)) == len(new_word):
        result += 1

print(result)