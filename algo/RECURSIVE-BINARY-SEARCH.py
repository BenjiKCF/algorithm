def recursive_binary_search(A,p,r,x):
    if p > r:
        return 'NOT-FOUND'
    else:
        q = (p + r) /2
        if A[q] == x:
            return q
        elif A[q] > x:
            return recursive_binary_search(A,p,q-1,x)
        else:
            return recursive_binary_search(A,q+1,r,x)


A = ['a','b','c','d']
p = 0
r = 3
x = 'c'

print recursive_binary_search(A,p,r,x)
