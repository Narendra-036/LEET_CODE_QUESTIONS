class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        a = []
        n = len(heights)
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(a, diff)
            if len(a) > ladders:
                bricks = bricks-heapq.heappop(a)
            if bricks < 0:
                return i
        
        return n-1