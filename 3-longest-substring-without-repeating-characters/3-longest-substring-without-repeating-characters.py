class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = [-1] * 128
        res, start_idx = 0, 0
        for end_idx, char in enumerate(s):
            if prev[ord(char)] >= start_idx:
                start_idx = prev[ord(char)] + 1
            prev[ord(char)] = end_idx
            res = max(res, end_idx - start_idx + 1)
            
        return res