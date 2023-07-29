# O(n) time | O(1) space
def isPalindrome(string):
    # Write your code here.
    li = 0
    ri = len(string) - 1
    while li < ri:
        if string[li] != string[ri]:
            return False
        li += 1
        ri -= 1
    return True