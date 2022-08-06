class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x=[]
        for i in grid:
            x+=i
        x.sort()
        for i in range(len(x)):
            if x[i]>=0:
                return i
        return len(x)