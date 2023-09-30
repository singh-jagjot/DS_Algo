# O(n) time | O(1) space
def kadanesAlgorithm(array):
    # Write your code here.
    maxEndingHere = array[0]
    currentMaxSum = array[0]

    for idx in range(1, len(array)):
        maxEndingHere = max(maxEndingHere + array[idx], array[idx])
        currentMaxSum = max(maxEndingHere, currentMaxSum)
    return currentMaxSum