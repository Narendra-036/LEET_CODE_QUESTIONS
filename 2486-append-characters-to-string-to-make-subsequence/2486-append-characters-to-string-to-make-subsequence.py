class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        i = j = 0
        while i < S and j < T:
            if s[i] == t[j]:
                j += 1
            i += 1
        return T - j