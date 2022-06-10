class Solution:
    def generate(self, x: int) -> List[List[int]]:
        a=[[1]*x for x in range(1,x+1)]
        for i in range(x):
            for j in range(1,len(a[i])-1):
                a[i][j]=a[i-1][j-1]+a[i-1][j]
        return a