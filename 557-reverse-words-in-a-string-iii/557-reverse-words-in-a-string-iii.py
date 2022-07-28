class Solution:
    def reverseWords(self, s: str) -> str:
        arr=map(str,s.split())
        ans=""
        for word in arr:
            
            
            
            ans+=word[::-1]
            ans+=" "
            
        return ans[:-1]