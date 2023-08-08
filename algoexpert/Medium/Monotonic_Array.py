# O(n) time | O(1) space
def isMonotonic(array):
    # Write your code here.
    isIncreasing = True
    isDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isIncreasing = False
        if array[i] > array[i - 1]:
            isDecreasing = False

    return isIncreasing or isDecreasing
