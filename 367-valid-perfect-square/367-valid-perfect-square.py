class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a=int(sqrt(num))
        if sqrt(num)==a:
            return True
        return False