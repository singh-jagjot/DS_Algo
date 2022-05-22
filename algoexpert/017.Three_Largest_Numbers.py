from typing import List


def threeLargest(arr: List) -> List:
    ans = [-float('inf'), -float('inf'), -float('inf')]
    for num in arr:
        if num > ans[2]:
            ans[0] = ans[1]
            ans[1] = ans[2]
            ans[2] = num
        elif num > ans[1]:
            ans[0] = ans[1]
            ans[1] = num
        elif num > ans[0]:
            ans[0] = num

    return ans


print(threeLargest([2, -4, 1, 6, 9]))
print(threeLargest([141,1,17,-7,-17,-27,18,541,8,7,7]))
print(threeLargest([-100,-98,-1,2,3,4]))

