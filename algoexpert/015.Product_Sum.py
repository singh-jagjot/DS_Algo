from typing import List


# Iterative Solution O(n) time | O(n) space [This solution is not tested]
def product_sum1(arr: str) -> int:
    stack = []
    depth = 0
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
            sub_sum = 0
            while True:
                temp = stack.pop()
                if temp == '[':
                    break
                sub_sum += temp
            stack.append(sub_sum * depth)
            depth -= 1

    return stack[0]


# Recursive Solution O(n) time | O(depth) space
def product_sum2(arr: List, depth=1) -> int:
    sub_sum = 0
    for idx, val in enumerate(arr):
        if type(val) == list:
            arr[idx] = product_sum2(val, depth + 1)
        sub_sum += arr[idx]
    return sub_sum * depth


print(product_sum2([5, 2, [7, -1], 3, [6, [-13, [5, 10, -5], 8], 4]]))
print(product_sum1('[[],[[[5,6]]]]'))
