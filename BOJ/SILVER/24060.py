def merge_sort(A, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            temp[t] = A[i]
        else:
            temp[t] = A[j]

    while i <= q:
        temp[t] = A[i]
    while j <= r:
        