class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=0:
            return ""
        start=0
        end=0
        for i in range(len(s)):
            l1=self.check(s,i,i)
            l2=self.check(s,i,i+1)
            mlen=max(l1,l2)
            if mlen>end-start:
                start=i-(mlen-1)//2
                end=i+mlen//2
        return s[start:end+1]
    def check(self,x,a,b):
        while(a>=0 and b<len(x) and x[a]==x[b]):
            a-=1
            b+=1
        return b-a-1