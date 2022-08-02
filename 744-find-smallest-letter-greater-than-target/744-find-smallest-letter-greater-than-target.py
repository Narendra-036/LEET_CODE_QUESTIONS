class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand
        