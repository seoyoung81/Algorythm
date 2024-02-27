def isParenthesis(lst):
  stack = []
  for char in lst:
    if char == '(':
      stack.append(char)
    else:
      if not stack:
        stack.append(char)
      else:
        if stack[-1] == '(':
          stack.pop()
        else:
          stack.append(char)
  if stack:
    print("NO")
  else:
    print("YES")

n = int(input())
for _ in range(n):
  lst = list(str(input()))
  isParenthesis(lst)