
def recursive_linear_search(A, n, i, x):
    i = i - 1
    n = n - 1
    if i > n:
        return 'NOT-FOUND'
    else:
        if A[i] == x:
            return i
        else:
            i = i + 1
            n = n + 1
            return recursive_linear_search(A,n,i+1,x)

A = ['a','b','c','d']
n = 4
i = 0
x = 'a'

print recursive_linear_search(A, n, i, x)
