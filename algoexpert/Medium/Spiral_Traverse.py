# O(n) time | O(n) space
def spiralTraverse(array):
    # Write your code here.
    spiralArray = []
    rowStartIdx = colStartIdx = 0
    rowEndIdx = len(array) - 1
    colEndIdx = len(array[0]) - 1
    while rowStartIdx <= rowEndIdx and colStartIdx <= colEndIdx:
        for col in range(colStartIdx, colEndIdx + 1):
            spiralArray.append(array[rowStartIdx][col])
        # print(spiralArray)
        for row in range(rowStartIdx + 1, rowEndIdx):
            spiralArray.append(array[row][colEndIdx])
        # print(spiralArray)
        for col in range(colEndIdx, colStartIdx - 1, -1):
            if rowStartIdx == rowEndIdx:
                break
            spiralArray.append(array[rowEndIdx][col])
        # print(spiralArray)
        for row in range(rowEndIdx - 1, rowStartIdx, -1):
            if colStartIdx == colEndIdx:
                break
            spiralArray.append(array[row][colStartIdx])
        # print(spiralArray)
        rowStartIdx += 1
        rowEndIdx -= 1
        colStartIdx += 1
        colEndIdx -= 1
    return spiralArray