# O(n^2) time | O(1) space
def selectionSort(array):
    # Write your code here.
    currentIndex = 0
    while currentIndex < len(array) - 1:
        smallestIndex = currentIndex
        for i in range(currentIndex + 1, len(array)):
            if array[smallestIndex] > array[i]:
                smallestIndex = i
        array[currentIndex], array[smallestIndex] = array[smallestIndex], array[currentIndex]
        currentIndex += 1

    return array
