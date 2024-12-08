A, B = map(int, input().split())

result = 0
while True:
  if A == B:
    result += 1
    break
  elif A > B:
    result = -1
    break
  else:
    if B % 2 == 0:
      # B를 2로 나누기
      B //= 2
      result += 1
    else:
      # 일의 자리 1인 경우
      if str(B)[-1] == '1':
        b = str(B)
        B = int(b[:len(b)-1])
        result += 1
      else:
        result = -1
        break

print(result)