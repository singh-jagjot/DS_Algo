# O(n) time | O(1) space [dict can have max 26 keys!]
def firstNonRepeatingCharacter(string):
    # Write your code here.
    alpha = dict()
    for char in string:
        if char not in alpha:
            alpha[char] = 1
        else:
            alpha[char] += 1

    for i,char in enumerate(string):
        if alpha[char] == 1:
            return i
    return -1
