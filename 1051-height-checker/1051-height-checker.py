class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=[x for x in heights]
        h.sort()
        count=0
        for i in range(len(h)):
            
            if h[i]!=heights[i]:
                count+=1
        return count