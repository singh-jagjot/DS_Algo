from typing import List


def sortedSquaredArray(array):
    # Write your code here.
    pivot = 0

    for val in array:
        if val < 0:
            pivot +=1

    left = pivot - 1
    right = pivot

    ans = []

    while left >= 0 and right < len(array) :
        val1 = array[left]**2
        val2 = array[right]**2

        if  val1 > val2:
            ans.append(val2)
            right +=1
        else:
            ans.append(val1)
            left -=1

    if left < 0:
        while right < len(array):
            ans.append(array[right] **2)
            right +=1
    else:
        while left >= 0:
            ans.append(array[left] **2)
            left -=1
    return ans



# Better solution with same time complexity but with less code


def sorted_square_array(nums: List[int]) -> List[int]:
    sarr = [0 for _ in nums]
    smaller_value_idx = 0
    larger_value_idx = len(nums) - 1

    for idx in reversed(range(len(nums))):
        smaller_value = nums[smaller_value_idx]
        larger_value = nums[larger_value_idx]

        if abs(smaller_value) > abs(larger_value):
            sarr[idx] = smaller_value * smaller_value
            smaller_value_idx += 1
        else:
            sarr[idx] = larger_value * larger_value
            larger_value_idx -= 1
    return sarr
