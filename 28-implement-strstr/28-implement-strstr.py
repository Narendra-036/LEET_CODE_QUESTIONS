class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0
        b=len(needle)
        for i in range(len(haystack)-b+1):
            print(1)
            if haystack[i:i+b]==needle:
                return i
        return -1
            
        