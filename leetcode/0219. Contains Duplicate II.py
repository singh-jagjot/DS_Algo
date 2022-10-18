class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for idx, num in enumerate(nums):
            if num not in seen:
                seen[num] = idx
            else:
                if idx - seen[num] <= k:
                    return True
                seen[num] = idx
        return False
