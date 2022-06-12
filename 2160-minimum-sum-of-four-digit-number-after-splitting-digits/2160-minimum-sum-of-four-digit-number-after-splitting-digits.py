class Solution:
    def minimumSum(self, num: int) -> int:
        num=str(num)
        a=[i for i in num]
        a.sort()
        b=int(a[0])*10+int(a[3])
        c=int(a[1])*10+int(a[2])
        return b+c
        