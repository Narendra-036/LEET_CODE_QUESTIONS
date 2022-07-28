class Solution:
    def reverseWords(self, s: str) -> str:
        arr=list(map(str,s.split()))
        ans=""
        arr=arr[::-1]
        for i in arr:
            ans+=i
            ans+=" "
        return ans[:-1]