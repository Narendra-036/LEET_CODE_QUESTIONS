class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x=edges[0]
        count=0
        
        for i in edges:
            if x[0] in i:
                count+=1
            
        
        if count==len(edges):
            return x[0]
        else:
            return x[1]