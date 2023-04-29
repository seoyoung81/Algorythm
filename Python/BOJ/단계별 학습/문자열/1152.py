sentence = list(map(str, input().split(' ')))     # 문장 문자열 입력받은 걸 공백을 기준으로 쪼개서 리스트로 만들기
# print(sentence) ['The', 'Curious', 'Case', 'of', 'Benjamin', 'Button']

# 앞 뒤 공백을 제거하자



if sentence[0] == '':
    sentence.remove('')
if sentence[-1] == '':
    sentence.remove('')
    
# print(sentence)

print(len(sentence))
