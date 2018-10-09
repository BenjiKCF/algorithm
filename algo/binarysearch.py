def binary_search(arrays, target):
    minimum = 0
    maximum = len(arrays) - 1
    guess = int(minimum + maximum) / 2
    while minimum <= maximum:
        if arrays[guess] == target:
            return guess
        elif arrays[guess] < target:
            minimum = guess + 1
        elif arrays[guess] > target:
            maximum = guess - 1
        guess = int(minimum + maximum) / 2

arrays = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print binary_search(arrays, 29)
