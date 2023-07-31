from typing import List

# Recursive Solution O(n) time | O(depth) space
def productSum(array):
    return helper(array)

def helper(array, depth = 1):
    sum = 0
    for x in array:
        if isinstance(x, list):
            sum += helper(x, depth + 1)
        else:
            sum += x
    return sum * depth

