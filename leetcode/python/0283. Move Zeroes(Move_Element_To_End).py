class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_idx = -1
        for idx, val in enumerate(nums):
            if val == 0 and zero_idx == -1:
                zero_idx = idx
            elif val != 0 and zero_idx != -1:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
                zero_idx += 1