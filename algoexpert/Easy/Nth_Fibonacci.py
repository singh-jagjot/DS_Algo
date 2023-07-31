# Iterative
# O(n) time| O(1) space [O(1)
def getNthFib(n):
    # Write your code here.
    a = 1
    b = 1
    flag = 3
    while flag < n:
        b = a + b
        a = b - a
        flag += 1
   
    return b if n > 1 else 0

