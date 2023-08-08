# Time O(nlog(n) + mlog(m)) | Space O(1)
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = idxTwo = 0
    smallest = float('inf')
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        current = abs(firstNum - secondNum)
        if firstNum == secondNum:
            return [firstNum, secondNum]
        elif firstNum < secondNum:
            idxOne += 1
        else:
            idxTwo += 1

        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair
