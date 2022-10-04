class Solution:
    def tribonacci(self, n: int) -> int:
        x=0
        y=1
        z=1
        
        for i in range(n-3+1):
            temp1=x
            temp2=y
            x=y
            y=z
            z=z+temp1+temp2
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        return z