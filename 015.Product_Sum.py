from time import sleep
from typing import List

# Iterative Solution O(n) time | O(n) space [This solution is not tested]
def productSum1(arr: str) -> int:
    stack = []
    depth = 0
    ans = 0
    num = ''
    sign = 1
    for x in arr:
        # print(stack)
        if x == '[':
            depth += 1
            stack.append(x)
        elif x == '-':
            sign *= -1
        elif x.isnumeric():
            num += x
        elif x == ',':
            if num != '':
                stack.append(int(num) * sign)
                sign = 1
            num = ''
        else:
            if num != '':
                stack.append(int(num) * sign)
                sign = 1
            num = ''
            # stack.append(']')
            subSum = 0
            while True:
                temp = stack.pop()
                if temp == '[':
                    break
                subSum += temp
            stack.append(subSum * depth)
            depth -= 1
            
    return stack[0]


# Recursive Solution O(n) time | O(depth) space
def productSum2(arr: List, depth = 1) -> int:
    subSum = 0
    for idx, val in enumerate(arr):
        if type(val) == list:
            arr[idx] =  productSum2(val, depth + 1)
        subSum += arr[idx]
    return subSum * depth

print(productSum2([5,2,[7,-1],3,[6,[-13,[5,10,-5],8],4]]))
print(productSum1('[[],[[[5,6]]]]'))