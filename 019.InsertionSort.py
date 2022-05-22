from typing import List


def insertionSort(arr: List) -> List:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

print(insertionSort([2,5,3,4,8,-7,5]))