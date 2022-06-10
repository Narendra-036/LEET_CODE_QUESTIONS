class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        m=1
        while(n!=0):
            a=n%10
            s+=a
            m*=a
            n=n//10
        return m-s