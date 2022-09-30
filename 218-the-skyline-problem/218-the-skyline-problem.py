class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
       
        x = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, "doesn't matter") for _, R, _ in buildings])   
        result, max_heap = [[0, 0]], [(0, float('inf'))]
        
        for x, i, R in x:
            while x >= max_heap[0][1]:
                heapq.heappop(max_heap)
            if i:
                heapq.heappush(max_heap, (i, R))
            curr_max_height = -max_heap[0][0]
            if result[-1][1] != curr_max_height:
                result.append([x, curr_max_height])
        return result[1:] 