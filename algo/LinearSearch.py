def linear_search(A, x):
    answer = 'Not found'
    for i in range(0, len(A)):
        if A[i] == x:
            answer = i
    return answer


A = ['a','b','c','d']
print linear_search(A, 'e')
