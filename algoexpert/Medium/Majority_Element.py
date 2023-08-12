# O(n) time | O(1) space
def majorityElement(array):
    # Write your code here.
    count = 0
    majEle = None
    for val in array:
        if count == 0:
            majEle = val
            
        if val == majEle:
            count += 1
        else:
            count -= 1
    return majEle
