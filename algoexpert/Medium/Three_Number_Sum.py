# O(n^2) time | O(n) space (We can end up storing all the elements in triplets array)
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i,x in enumerate(array):
        left = i + 1
        right = len(array) - 1
        while left < right:
            leftVal = array[left]
            rightVal = array[right]
            sum = x + leftVal + rightVal
            if sum == targetSum:
                triplets.append([x, leftVal,rightVal])
                left += 1
                right -= 1
            elif sum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets
