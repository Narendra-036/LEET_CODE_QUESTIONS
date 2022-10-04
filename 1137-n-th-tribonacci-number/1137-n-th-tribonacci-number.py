class Solution:
    def tribonacci(self, n: int) -> int:
        a=[0,1,1]
        for i in range(n-3+1):
            a.append(sum(a[-3:]))
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        return a[-1]
            