# O(rows * columns) time | O(rows * columns) space
def transposeMatrix(matrix):
    # Write your code here.
    rows = len(matrix)
    cols = len(matrix[0])

    mat = []
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        mat.append(row)
            
    return mat
