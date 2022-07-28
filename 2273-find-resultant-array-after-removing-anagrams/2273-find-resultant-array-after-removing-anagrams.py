class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev = None
        for w in words:
            count = Counter(w)
            if count != prev:
                res.append(w)
                prev = count
        return res