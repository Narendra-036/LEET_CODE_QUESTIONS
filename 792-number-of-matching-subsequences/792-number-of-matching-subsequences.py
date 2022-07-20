class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        r = 0
    
        n = len(s)
        d = {}
        for word in words:
            d[word] = d.get(word,0) + 1
    
        for word in d.keys():
            i = j = 0
        
            while i < n and j < len(word):
            
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                
            if j == len(word):
                r += 1*d[word]
        return r