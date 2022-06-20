from typing import List


# Time O(nlog(n) + mlog(m)) | Space O(1)
def smallest_difference(arr1: List, arr2: List) -> List:
    arr1.sort()
    arr2.sort()
    idx1 = idx2 = 0
    curr_ans = [arr1[idx1], arr2[idx2]]
    curr_diff = float('inf')
    while idx1 < len(arr1) and idx2 < len(arr2):
        temp = abs(arr1[idx1] - arr2[idx2])
        temp_pair = [arr1[idx1], arr2[idx2]]
        if temp == 0:
            return temp_pair

        if temp < curr_diff:
            curr_diff = temp
            curr_ans = temp_pair

        if arr1[idx1] < arr2[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    return curr_ans


print(smallest_difference([-1, 3, 5, 10, 20, 28], [15, 17, 26, 134, 135]))
