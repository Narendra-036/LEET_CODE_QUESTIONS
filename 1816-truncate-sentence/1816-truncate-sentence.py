class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans=list(map(str,s.split()[:k]))
        a=""
        for i in ans:
            
            a+=i
            a+=" "
        a=a[:-1]
        return a
        
        