class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x=edges[0]
        
        for i in edges:
            if x[0] not in i:
                return x[1]
        return x[0]