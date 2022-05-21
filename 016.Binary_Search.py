from typing import List

# Recursive
def binarySearch(arr: List, target) -> bool:
    return binarySearchHelper(arr, target, 0, len(arr) - 1)


def binarySearchHelper(arr: List, target: int, left: int, right: int) -> bool:
    if left > right:
        return False

    mid = (left + right) // 2

    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return binarySearchHelper(arr, target, left, mid - 1)
    else:
        return binarySearchHelper(arr, target, mid + 1, right)

#Iterative
def binarySearchItr(arr: List, target: int) -> bool:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(binarySearchItr([1, 3, 4, 6, 7, 9, 23], 23))
