def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    numSet = set()
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right-=1
            elif sum < 0:
                left+=1
            else:
                ans.append([nums[left], nums[i], nums[right]])
                left+=1
                right-=1
    return ans