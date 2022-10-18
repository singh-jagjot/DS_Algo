class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            value = abs(num)
            if nums[value - 1] > 0:
                nums[value - 1] = -nums[value - 1] 
            elif nums[value - 1] < 0:
                res.append(value)
        return res
