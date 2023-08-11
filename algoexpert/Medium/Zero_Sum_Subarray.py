# O(n) time | O(n) space
def zeroSumSubarray(nums):
    # Write your code here.
    sums = set()
    sums.add(0)
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)
    return False

print(zeroSumSubarray([-5,-5,2,3,-2]))
print(zeroSumSubarray([-1,5,4,3,-3,-2]))
print(zeroSumSubarray([0]))
