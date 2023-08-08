class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_idx = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[next_idx] = nums[i]
                next_idx += 1
                count = 1
            elif count < 2:
                count += 1
                nums[next_idx] = nums[i]
                next_idx += 1

        return next_idx

# More elegant solution:
# def removeDuplicates(self, nums):
#     i = 0
#     for n in nums:
#         if i < 2 or n > nums[i-2]:
#             nums[i] = n
#             i += 1
#     return i
# For those who have trouble grasping the logic, the key is that num[i] is replaced by the value of the current element and i steps forward,
# but stops replacing if nums[i-2] = current, indicating that the current identical sequence has the maximum length of 2. Essentially,
# we are walking through the array and copying over each element to the left pointer unless the last sequence of identical elements
# hits the limit of length 2... then we wait until we find a new element and start copying over again.
