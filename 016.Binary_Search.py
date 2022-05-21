from typing import List


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


print(binarySearch([1, 3, 4, 6, 7, 9, 23], 233))
