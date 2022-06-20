import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        x=np.array(grid)
        for i in range(len(x)):
            for j in range(len(x[0])):
                x[i][j]=min(max(x[i]),max(x[:,j]))
        ans=0
        for i in range(len(x)):
            for j in range(len(x[0])):
                ans+= x[i,j]-grid[i][j]
                
        return ans
                