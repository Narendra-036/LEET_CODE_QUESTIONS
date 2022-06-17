class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        x=num
        x=str(num)
        x=x[::-1]
        x=int(x)
        x=str(x)
        x=x[::-1]
        x=int(x)
        return x==num