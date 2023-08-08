# Better solution as here order of the elements(other) is preserved.
# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    swapIdx = 0
    for i in range(len(array)):
        num = array[i]
        if num != toMove:
            if swapIdx != i:
                array[swapIdx], array[i] = num, toMove
            swapIdx += 1
    return array
