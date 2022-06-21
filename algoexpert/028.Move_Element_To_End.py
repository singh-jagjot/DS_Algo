from typing import List


# Better solution as here order of the elements(other) is preserved.
def mete(nums: List, val):
    val_idx = -1
    for idx, num in enumerate(nums):
        if num == val and val_idx == -1:
            val_idx = idx
        elif num != val and val_idx != -1:
            nums[idx], nums[val_idx] = nums[val_idx], nums[idx]
            val_idx += 1


lst = [2, 1, 2, 2, 2, 3, 4, 2]
mete(lst, 2)
print(lst)
