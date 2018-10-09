def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i - 1
        while j > -1 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


A = [12,9,3,7,14,11]
print insertion_sort(A)

# key = 9
# j = 0
# while 0 > -1 and 12 > 9:
# [12,12,3,7,14,11]
# j = -1
# A[0] = 9 [9,12,3,7,14,11]

def insertion_sort1(A):
    n = len(A)
    for i in range(1,n):
        j = i - 1
        while j > -1 and A[j] > A[i]:
            A[i], A[j] = A[j], A[i]
    return A

print insertion_sort1(A)
