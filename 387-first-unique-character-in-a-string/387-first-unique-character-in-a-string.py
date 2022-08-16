class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=collections.Counter(s)
        for i,j in enumerate(s):
            if(count[j]==1):
                return i
        return -1