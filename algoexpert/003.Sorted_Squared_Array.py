from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    parr = []  # Sorted in Ascending
    narr = []  # Sorted in Descending
    sarr = []
    for x in nums:
        if x >= 0:
            parr.append(x*x)
        else:
            narr.append(x*x)

    if len(narr) == 0:
        return parr
    if len(parr) == 0:
        return narr[::-1]

    pidx = 0
    nidx = len(narr) - 1

    while pidx < len(parr) and nidx > -1:
        if parr[pidx] < narr[nidx]:
            sarr.append(parr[pidx])
            pidx += 1
        else:
            sarr.append(narr[nidx])
            nidx -= 1

    while pidx < len(parr):
        sarr.append(parr[pidx])
        pidx += 1
    while nidx > -1:
        sarr.append(narr[nidx])
        nidx -= 1

    return sarr


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
