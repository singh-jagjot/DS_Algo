from typing import List


# O(N) time | O(N) space
def first_duplicate_value1(array: List):
    seen = set()
    for x in array:
        if x in seen:
            return x
        seen.add(x)
    return -1


# Better(works only if array contains 1..N numbers) with O(N) time | O(1) space
def first_duplicate_value2(array: List):
    for x in array:
        val = abs(x)
        if array[val - 1] < 0:
            return val
        array[val - 1] *= -1
    return -1


print(first_duplicate_value2([1, 3, 2, 5, 3, 6, 3]))
