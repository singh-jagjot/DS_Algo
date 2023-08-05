# Iterative
# O(log(n)) Time | O(1) Space
def binarySearchI(array, target):
    # Write your code here.
    return helperIterative(array, target)

def helperIterative(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# Recursive
# O(log(n)) Time | O(log(n)) Space
def binarySearchR(array, target):
    # Write your code here.
    return helperRecursive(array, target, 0, len(array) - 1)


def helperRecursive(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right)//2
    val = array[mid]
    if val == target:
        return mid
    if target < val:
        return helperRecursive(array, target, left, mid - 1)
    else:
        return helperRecursive(array, target, mid + 1, right)
