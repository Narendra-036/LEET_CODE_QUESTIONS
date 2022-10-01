def fun(s,i,memo):
    if(i==len(s)):
        return 1
    if(s[i]=="0"):
        return 0
    if(memo[i]>=0):
        return memo[i]
    a=fun(s,i+1,memo)
    b=0
    if(i<len(s)-1 and int(s[i:i+2])<=26):
        b=fun(s,i+2,memo)
    memo[i]=a+b
    return a+b
class Solution:
    def numDecodings(self, s: str) -> int:
        memo=defaultdict(lambda:-1)
        return fun(s,0,memo)