def better_linear_search(A, x):
    for i in range(0, len(A)):
        if A[i] == x:
            return i
    return "Not found"


A = ['a','b','c','d']
print better_linear_search(A, 'd')
