# Iterative
def fibonacci(n: int) -> int:
    a = 0
    b = 1
    flag = 0
    while flag < n - 1:
        b = a + b
        a = b - a
        flag += 1
    return b


# Recursive
# O(n) time| O(n) space [O(1) with tail recursion optimization]
def fibonacci2(n: int, count=0, a=0, b=1) -> int:
    if n == 0:
        return 0
    if count == n:
        return a
    b = a + b
    a = b - a
    return fibonacci2(n, count + 1, a, b)
