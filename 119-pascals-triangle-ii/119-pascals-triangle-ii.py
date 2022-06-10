class Solution:
    def getRow(self, x: int) -> List[int]:
        a=[[1]*x for x in range(1,x+2)]
        for i in range(x+1):
            for j in range(1,len(a[i])-1):
                a[i][j]=a[i-1][j-1]+a[i-1][j]
        return a[x]
        