from typing import List


# Recursive
def binary_search(arr: List, target) -> bool:
    return binary_search_helper(arr, target, 0, len(arr) - 1)


def binary_search_helper(arr: List, target: int, left: int, right: int) -> bool:
    if left > right:
        return False

    mid = (left + right) // 2

    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return binary_search_helper(arr, target, left, mid - 1)
    else:
        return binary_search_helper(arr, target, mid + 1, right)


# Iterative
def binary_search_iterative(arr: List, target: int) -> bool:
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


print(binary_search_iterative([1, 3, 4, 6, 7, 9, 23], 23))
