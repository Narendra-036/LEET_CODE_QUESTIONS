class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l,t=0,0
        r,b=n,n
        a= [[0 for x in range(n)] for y in range(n)]
        
        print(a)
        num=1
        while l<r and t<b:
            for i in range(l,r):
                a[t][i]=num
                num+=1
            t+=1
            for i in range(t,b):
                a[i][r-1]=num
                num+=1
            r-=1
            
            for i in range(r-1,l-1,-1):
                a[b-1][i]=num
                num+=1
            b-=1
            for i in range(b-1,t-1,-1):
                a[i][l]=num
                num+=1
            l+=1
        return a