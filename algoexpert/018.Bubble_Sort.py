from typing import List


def bubbleSort(arr: List) -> List:
    count = 0
    isSorted = False
    while not isSorted:
        isSorted = True
        for idx in range(len(arr) - 1 - count):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                isSorted = False
        
        count += 1

    return arr

print(bubbleSort([5,2,7,6,1,4]))