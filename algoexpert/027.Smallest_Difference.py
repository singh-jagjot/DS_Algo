from typing import List

# Time O(nlog(n) + mlog(m)) | Space O(1)
def smallestDifference(arr1: List, arr2: List) -> List:
    arr1.sort()
    arr2.sort()
    idx1 = idx2 = 0
    currAns = [arr1[idx1], arr2[idx2]]
    currDiff = float('inf')
    while idx1 < len(arr1) and idx2 < len(arr2):
        temp = abs(arr1[idx1] - arr2[idx2])
        tempPair = [arr1[idx1], arr2[idx2]]
        if temp == 0:
            return tempPair
        
        if temp < currDiff:
            currDiff = temp
            currAns = tempPair

        if arr1[idx1] < arr2[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    return currAns


print(smallestDifference([-1, 3, 5, 10, 20, 28], [15, 17, 26, 134, 135]))
