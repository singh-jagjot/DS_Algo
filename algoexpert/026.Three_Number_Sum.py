from typing import List


def three_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                ans.append([nums[left], nums[i], nums[right]])
                left += 1
                right -= 1
    return ans
