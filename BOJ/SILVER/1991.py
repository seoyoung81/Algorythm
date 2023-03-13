N = int(input())    # 노드의 개수
tree = {}
for i in range(N):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]

def pre_order(T):
    if T != '.':
        print(T, end='')
        pre_order(tree[T][0])
        pre_order(tree[T][1])

def in_order(T):
    if T != '.':
        in_order(tree[T][0])
        print(T, end='')
        in_order(tree[T][1])

def post_order(T):
    if T != '.':
        post_order(tree[T][0])
        post_order(tree[T][1])
        print(T, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')