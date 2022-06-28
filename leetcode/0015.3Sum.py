class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        # print(len(nums))
        previous = None
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right and nums[i] != previous:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                    while right > -1 and nums[right] == nums[right+1]:
                        right-=1
                elif sum < 0:
                    left += 1
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left+=1
                else:
                    ans.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1

                    while right > -1 and nums[right] == nums[right+1]:
                        right-=1
            previous = nums[i]
        return ans