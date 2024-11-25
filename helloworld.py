import random

print("Hello world!")

def binary_search(lis, target):
    high = len(lis)-1
    low = 0
    while high >= low:
        middle = (high + low) // 2
        if lis[middle] == target:
            return middle
        elif lis[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

test_list = [3, 5, 6, 7, 9, 10, 11, 15, 16, 20]
print(binary_search(test_list, 3))
print(binary_search(test_list, 7))
print(binary_search(test_list, 20))
print(binary_search(test_list, 1))