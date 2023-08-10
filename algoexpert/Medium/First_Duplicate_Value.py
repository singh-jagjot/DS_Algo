# O(n) time | O(1) space
def firstDuplicateValue(array):
    # Write your code here.
    for x in array:
        absValue = abs(x)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1