class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]
        left_product = right_product = 1
        for i in range(len(nums)):
            products[i] = left_product
            left_product *= nums[i]

        for i in reversed(range(len(nums))):
            products[i] *= right_product
            right_product *= nums[i]

        return products