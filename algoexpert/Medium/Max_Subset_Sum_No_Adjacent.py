# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    first = array[0]
    second = max(first, array[1])

    for i in range(2, len(array)):
        current = max(second, first + array[i])
        first, second = second, current
    return second
