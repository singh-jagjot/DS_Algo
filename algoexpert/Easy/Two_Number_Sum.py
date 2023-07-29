# O(n) time | O(n) Space
def twoNumberSum(array, targetSum):
    # Write your code here.
    s = {val for val in array}
    
    for val in array:
        if targetSum - val in s and val != targetSum - val:
            return [val, targetSum - val]
    return []
        
# O(nlog(n)) time | O(1) Space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        val1 = array[left]
        val2 = array[right]
        sum = val1 + val2
        if sum == targetSum:
            return [val1, val2]
        elif sum < targetSum:
            left += 1
        else:
            right -= 1

    return []
