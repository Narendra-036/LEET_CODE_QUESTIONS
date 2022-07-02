class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        max_width, max_height = max(horizontalCuts[0], h - horizontalCuts[-1]), max(verticalCuts[0], w - verticalCuts[-1])
        
        if len(horizontalCuts) > 1:
            for index_1 in range(1, len(horizontalCuts)):
                max_width = max(max_width, horizontalCuts[index_1] - horizontalCuts[index_1 - 1])
        if len(verticalCuts) > 1:
            for index_2 in range(1, len(verticalCuts)):
                max_height = max(max_height, verticalCuts[index_2] - verticalCuts[index_2 - 1])
                
        return (max_height * max_width) % (10**9 + 7)