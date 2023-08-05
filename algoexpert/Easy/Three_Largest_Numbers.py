# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    # Write your code here.
    ans = [-float('inf'), -float('inf'), -float('inf')]
    for num in array:
        if num > ans[2]:
            ans[0] = ans[1]
            ans[1] = ans[2]
            ans[2] = num
        elif num > ans[1]:
            ans[0] = ans[1]
            ans[1] = num
        elif num > ans[0]:
            ans[0] = num

    return ans