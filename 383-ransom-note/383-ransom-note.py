class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = [0] * 26
        magazine_counter = [0] * 26
        
        for c in ransomNote:
            ransom_counter[ord(c) - ord('a')] += 1
            
        for c in magazine:
            magazine_counter[ord(c) - ord('a')] += 1
            
        for alphabet in range(26):
            if magazine_counter[alphabet] < ransom_counter[alphabet]:
                return False
        
        return True