# O(n) time | O(1) space
def missingNumbers(nums):
    # Write your code here.
    total = sum(nums)
    # Sum of N terms of an AP is used here
    missingTotal = (len(nums) + 2) * (len(nums) + 3)//2 - total
    pivot = missingTotal//2
    firstHalfSum = secondHalfSum = 0
    for num in nums:
        if num <= pivot:
            firstHalfSum += num
        else:
            secondHalfSum += num
    # Sum of N terms of an AP is used here
    firstMissingNumber = (pivot + 1)*pivot//2 - firstHalfSum
    secondMisingNumber = missingTotal - firstMissingNumber
    return [firstMissingNumber, secondMisingNumber]


print(missingNumbers([1, 2, 3]))
