class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d={}
        for i in edges:
            if i[0] not in d:
                d[i[0]]=[i[1]]
            else:
                d[i[0]].append(i[1])
        x=[]
        for i in d:
            x+=d[i]
        x=set(x)
        ans=[]
        for i in range(n):
            if i not in x:
                ans.append(i)
        return ans
            