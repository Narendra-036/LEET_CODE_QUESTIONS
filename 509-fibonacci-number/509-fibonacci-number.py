class Solution:
    def fib(self, n: int) -> int:
        res, nxt = 0, 1
        for _ in range(n):
            res, nxt = nxt, res+nxt
        return res 