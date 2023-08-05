# O(n) time | O(n) space
def runLengthEncoding(string):
    # Write your code here.
    count = 1
    currentChar = string[0]
    ansList = []
    for i in range(1, len(string)):
        if string[i] != currentChar or count == 9:
            ansList.append(str(count))
            ansList.append(currentChar)
            currentChar = string[i]
            count = 1
        else:
            count += 1
    ansList.append(str(count))
    ansList.append(currentChar)
    return ''.join(ansList)
