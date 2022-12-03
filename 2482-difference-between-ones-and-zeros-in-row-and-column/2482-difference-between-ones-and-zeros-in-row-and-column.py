class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        x=[]
        for i in range(len(grid[0])):
            p=0
            for j in range(len(grid)):
                if grid[j][i]==1:
                    p+=1
            x.append(p)
        y=[]
        for i in range(len(grid)):
            y.append(sum(grid[i]))
        
        a=len(grid)
        b=len(grid[0])
        
        dif=[]
        
        for i in range(len(grid)):
            z=[]
            for j in range(len(grid[0])):
                
                # oro=sum(grid[i])
                # zr=len(grid[i])-oro
                # oc=x[j]
                # zc=len(grid)-oc
                # # print(oro,oc,zr,zc)
                z.append(x[j]+y[i]-a+x[j]-b+y[i])
            dif.append(z)
        return dif
        
        