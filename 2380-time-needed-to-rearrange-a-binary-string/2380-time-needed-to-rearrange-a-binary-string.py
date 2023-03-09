class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        if "01" in s:
            s=s.replace("01","10")
            return 1+self.secondsToRemoveOccurrences(s)
        return 0
        
#         steps, zeroes = 0, 0
#         for ch in s:
#             if ch == '0':
#                 zeroes += 1
#                 continue
#             if zeroes > 0:
#                 steps = max(1 + steps, zeroes)
                
#         return steps