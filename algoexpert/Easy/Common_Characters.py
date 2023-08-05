# O(n*m) time | O(m) space, n = size of strings, m = size of the longest string
def commonCharacters(strings):
    # Write your code here.
    smallestString = strings[0]
    for string in strings:
        if len(smallestString) > len(string):
            smallestString = string
    commonSet = set(smallestString)
    toRemoveList = []
    for string in strings:
        currentStringSet = set(string)
        for char in commonSet:
            if char not in currentStringSet:
                toRemoveList.append(char)
        for char in toRemoveList:
            if char in commonSet:
                commonSet.remove(char)

    return list(commonSet)

# O(n*m) time | O(c) space, n = size of strings, m = size of the longest string,
# c = number of unique characters across all strings
def commonCharacters(strings):
    # Write your code here.
    commonChars = []
    alpha = dict()
    for string in strings:
        alphaSet = set()
        for char in string:
            if char not in alphaSet:
                alphaSet.add(char)
                if char in alpha:
                    alpha[char] += 1
                else:
                    alpha[char] = 1

    for char, freq in alpha.items():
        if freq == len(strings):
            commonChars.append(char)
    return commonChars
