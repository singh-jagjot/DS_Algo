from typing import List

def selectionSort(arr: List) -> List:
    currentIdx = 0
    while currentIdx < len(arr) - 1:
        smallIdx = currentIdx
        for i in range(currentIdx + 1, len(arr)):
            if arr[smallIdx] > arr[i]:
                smallIdx = i
        arr[currentIdx], arr[smallIdx] = arr[smallIdx], arr[currentIdx]
        currentIdx += 1
    return arr

print(selectionSort([2,5,3,8,7,-50,-3,-4,5,6,4,6]))
