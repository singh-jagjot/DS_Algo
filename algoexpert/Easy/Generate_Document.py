# O(characters+document) time | O(c) space, where c is number of unique characters
def generateDocument(characters, document):
    # Write your code here.
    alpha = dict()
    for char in characters:
        if char in alpha:
            alpha[char] += 1
        else:
            alpha[char] = 1

    for char in document:
        if char not in alpha or alpha[char] == 0:
            return False
        alpha[char] -= 1
        
    return True
