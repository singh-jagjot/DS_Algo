class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        flag = 0
        if n == 0: return a
        while flag < n - 1:
            b = a + b
            a = b - a
            flag += 1
        return b