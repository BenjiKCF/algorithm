def binary_search(A,n,x):
    p, r = 0, n - 1
    while p <= r:
        q = (p+r) / 2
        if A[q] == x:
            return q
        else:
            if A[q] > x:
                r = q - 1
            else:
                p = q + 1
    return "NOT-FOUND"


A = ['a','b','c','d']
n = 4
x = 'b'

print binary_search(A,n,x)
