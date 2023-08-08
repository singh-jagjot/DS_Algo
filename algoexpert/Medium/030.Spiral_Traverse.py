from typing import List


def spiral_traverse(arr: List):
    start_row = 0
    end_row = len(arr) - 1
    start_col = 0
    end_col = len(arr[0]) - 1
    result = []
    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            result.append(arr[start_row][col])
        for row in range(start_row + 1, end_row):
            result.append(arr[row][end_col])
        for col in reversed(range(start_col, end_col + 1)):
            if start_row == end_row:
                break
            result.append(arr[end_row][col])
        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            result.append(arr[row][start_col])

        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1

    return result


arr = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
# arr = [[1,2,3,4]]
# arr = [[1],[2],[3],[4]]

print(spiral_traverse(arr))
