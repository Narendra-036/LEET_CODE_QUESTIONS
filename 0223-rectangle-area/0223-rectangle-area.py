class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x=[]
        for i in range(ax1,ax2):
            for j in  range(ay1,ay2):
                x.append([i,j])
        
        for i in range(bx1,bx2):
            for j in  range(by1,by2):
                if [i,j] not in x:
                    x.append([i,j])
        
        return len(x)