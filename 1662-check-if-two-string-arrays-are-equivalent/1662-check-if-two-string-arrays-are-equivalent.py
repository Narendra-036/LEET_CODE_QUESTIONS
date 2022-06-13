class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        a=""
        for i in word1:
            s+=i
        for i in word2:
            a+=i
        if a==s:
            return True
        return False
