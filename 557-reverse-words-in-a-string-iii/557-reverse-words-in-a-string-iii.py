class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        s=list(map(str,s.split()))
        for i in s:
            ans+=i[::-1]
            ans+=" "
        return ans[:-1]
    