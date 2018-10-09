# A = array
# n = number of elements
# x = value being searched
def sentinel_linear_search(A,n,x):
    A.append(A[n-1])
    A[n-1] = x

    i = 1
    while A[i] != x:
        i += 1
    A[n-1] = A[n]

    if i < n or A[n] == x:
        return i
    else:
        return 'NOT-FOUND'

A = ['a','b','c','d']
n = 4
x = 'c'
print sentinel_linear_search(A,n,x)
