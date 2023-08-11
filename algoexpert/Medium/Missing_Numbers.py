def missingNumbers(nums):
    # Write your code here.
    total = sum(nums)
    missing_sum = (len(nums) + 2) * (len(nums) + 3)//2 - total
    return missing_sum

print(missingNumbers([1,2,3]))
