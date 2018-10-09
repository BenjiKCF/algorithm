def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        smallest = i

        for j in range(i+1, n):
            if A[j] < A[smallest]:
                smallest = j

        A[i], A[smallest] = A[smallest], A[i]
    return A

A = [12,9,3,7,14,11]


print selection_sort(A)
