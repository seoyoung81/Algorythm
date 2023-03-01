# # import sys
# # sys.stdin = open('input.txt')
#
# for _ in range(4):
#     result = ''
#     x1, y1, x2, y2, a1, b1, a2, b2 = map(int, input().split())
#
#     # d
#     if x2 < a1 or a2 < x1 or b2 < y1 or y2 < b1:
#         result = 'd'
#
#     # c
#     elif a1 == x2 or x1 == a2:
#         if b1 == y2 or y1 == b2:
#             result = 'c'
#         else:
#             result = 'b'
#     # elif a2 == x1 or a1 == x2:
#     #     if b1 == y2 or y1 == b2:
#     #         result = 'c'
#     #     else:
#     #         result = 'b'
#
#     else:
#         result = 'a'
#
#     print(result)


for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # d
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')

    # c
    elif x1 == p2 or x2 == p1:
        if q1 == y2 or q2 == y1:
            print('c')
        # b
        else:
            print('b')
    # b
    elif q1 == y2 or q2 == y1:
        print('b')

    # a
    else:
        print('a')