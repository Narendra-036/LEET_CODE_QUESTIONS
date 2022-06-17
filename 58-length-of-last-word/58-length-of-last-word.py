class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=list(map(str,s.split()))
        return len(a[-1])