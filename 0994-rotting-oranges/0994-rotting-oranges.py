class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        c=[]
        x=len(grid)
        y=len(grid[0])
        for i in range(x):
            for j in range(y):
                if grid[i][j]==2:
                    c.append([i,j])
        # print(c)
        ans=0
        while len(c)!=0:
            temp=[]
            for k in range(len(c)):
                i=c[k][0]
                j=c[k][1]
                if i+1<x and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    temp.append([i+1,j])
                    
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    temp.append([i-1,j])
                    
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    temp.append([i,j-1])
                    
                if j+1<y and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    temp.append([i,j+1])
            ans+=1
            # print(grid)
            # print(temp)
            # print(len(temp))
            c=temp[:][:]
        for i in grid:
            if 1 in i:
                return -1
        if ans==0:
            return 0
        else:
            return ans-1
            
                    
                
        
        
        
#         c=0
#         x=len(grid)
#         y=len(grid[0])
#         ans=0
#         while True:
#             for i in range(x):
#                 for j in range(y):
#                     if grid[i][j]==2:
#                         if i+1<x and grid[i+1][j]==1:
#                             grid[i+1][j]=2
#                             c+=1
#                         if i-1>=0 and grid[i-1][j]==1:
#                             grid[i-1][j]=2
#                             c+=1
#                         if j-1>=0 and grid[i][j-1]==1:
#                             grid[i][j-1]=2
#                             c+=1
#                         if j+1<y and grid[i][j+1]==1:
#                             grid[i][j+1]=2
#                             c+=1
            
#             if c==0:
#                 break
#             ans+=1
#             c=0
#         print(grid)
#         print(ans)
                        
            