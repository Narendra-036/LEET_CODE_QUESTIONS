class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for x in t:
            if x in s and s.count(x)==t.count(x):
                s.replace(x,'')
            else:
                return x        