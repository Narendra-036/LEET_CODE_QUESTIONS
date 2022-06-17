class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            s=str(x)
            s=s[::-1]
        else:
            s=str(x)
            s=s[::-1]
            s="-"+s[:-1]
        x=int(s)
        if x>(2**31)-1 or x<-2**31:
            return 0
        
        return x
            
            